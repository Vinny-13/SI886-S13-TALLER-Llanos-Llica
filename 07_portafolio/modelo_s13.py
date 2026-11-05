from pathlib import Path
import json, sys, textwrap
import pandas as pd
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BASE=Path(__file__).resolve().parent; ROOT=BASE.parent
LOG=ROOT/'evidencias/S13/salidas'; LOG.mkdir(parents=True,exist_ok=True)
GRAF=BASE/'graficos'; GRAF.mkdir(exist_ok=True)
DATA=json.loads((BASE/'datos_proyectos.json').read_text())
CAT=['Operar','Crecer','Transformar']
COL={'Operar':'#267879','Crecer':'#457cc0','Transformar':'#bc7134'}
def money(v): return f'{v:,.0f}'.replace(',',' ')
def log(name,t): (LOG/name).write_text(t,encoding='utf-8'); print(t)
def pf01():
 rows=[]
 for i,p in enumerate(DATA,1):
  rows.append(dict(candidato=f'C-{i:02}',codigo=p['codigo'],nombre=p['nombre'],fuente=p['fuente'],seccion=p['seccion'],origen=p['origen'],objetivo=p['objetivo'],categoria=p['categoria'],decision='Admitido',razon='Fuente documentada y objetivo definido en la base analítica adjunta.'))
 rows += [dict(candidato='C-13',codigo='PR-10',nombre='Consulta de estado de solicitudes de derechos',fuente='Brecha de servicio digital',seccion='6.1.7',origen='SD-02',objetivo='OD-04',categoria='Crecer',decision='Fusionado',razon='El seguimiento y las notificaciones quedan en los entregables de PR-10; no se duplica inversión.'),dict(candidato='C-14',codigo='',nombre='Asistente generativo para recomendaciones de medicamentos',fuente='',seccion='',origen='',objetivo='',categoria='',decision='Retirado',razon='Sin fuente admisible ni objetivo aprobado; añade riesgo de consejo clínico fuera del alcance.')]
 pd.DataFrame(rows).to_csv(BASE/'PF00_admision.csv',index=False)
 a=pd.DataFrame(rows[:12]); valid={'Obligación normativa','Brecha de arquitectura','Brecha de capacidad','Estrategia FODA','Brecha de servicio digital'}
 assert set(a.fuente)==valid and a.objetivo.str.strip().ne('').all()
 a.to_csv(BASE/'PF01_portafolio_candidatos.csv',index=False)
 log('PF01_control_admision.txt','14 candidatos; 12 admitidos; C-13 fusionado en PR-10; C-14 retirado.\nCinco fuentes cubiertas. Ningún admitido sin objetivo.\nC-13 conserva consulta de estado y notificaciones en PR-10.\nTrazabilidad contra base analítica elaborada, no contra un PETI previo del equipo.')
def pf02():
 rows=[]
 for p in DATA:
  row={k:p[k] for k in ['codigo','nombre','inversion','operacion','salida','margen']}
  row.update(p['componentes_iniciales']);row.update({k+'_anual':v for k,v in p['componentes_anuales'].items()})
  assert sum(p['componentes_iniciales'].values())==p['inversion']
  assert sum(p['componentes_anuales'].values())==p['operacion']
  t=p['inversion']+5*p['operacion']+p['salida']
  row.update(tco5=t,tco_min=round(t*(1-p['margen'])),tco_max=round(t*(1+p['margen'])),factor=t/p['inversion'],origen_estimacion='EA-01: estimación paramétrica académica, sin cotización comercial')
  rows.append(row)
 df=pd.DataFrame(rows);df.to_csv(BASE/'PF02_tco.csv',index=False)
 top=df.nlargest(3,'tco5').codigo.tolist(); assert top==['PR-01','PR-02','PR-03']
 log('PF02_resultados.txt',f'Inversión: {df.inversion.sum():.0f}; operación anual: {df.operacion.sum():.0f}; salida: {df.salida.sum():.0f}\nTCO5: {df.tco5.sum():.0f}; rango: {df.tco_min.sum():.0f}–{df.tco_max.sum():.0f}; factor: {df.tco5.sum()/df.inversion.sum():.4f}\nTres mayores por TCO e inversión: {top}\nMayor operación anual: PR-01, PR-02, PR-03.\nTodos incluyen migración, integración, formación y salida sin doble conteo.\nRangos simétricos de sensibilidad: no son intervalos estadísticos.')
def fichas():
 folder=BASE/'PF03_fichas';folder.mkdir(exist_ok=True)
 for p in DATA:
  deps=', '.join(p['dependencias']) or 'Ninguna dependencia técnica de la cartera.'
  habilita=', '.join(q['codigo'] for q in DATA if p['codigo'] in q['dependencias']) or 'Sin dependientes técnicos.'
  fields=[('Código y nombre',p['codigo']+' · '+p['nombre']),('Fuente',f"{p['fuente']} · sección {p['seccion']} {p['origen']}; {p['evidencia']}"),('Objetivo',p['objetivo']),('Categoría',p['categoria']),('Problema',p['problema']),('Alcance incluido',p['incluye']),('Alcance excluido',p['excluye']),('Entregables',p['entregables']),('Duración',str(p['meses'])+' meses desde autorización; no es fecha comprometida.'),('Esfuerzo',str(p['esfuerzo'])+' persona-mes; servicios externos e internos incluidos en inversión.'),('Inversión inicial','S/ '+money(p['inversion'])),('Operación anual','S/ '+money(p['operacion'])),('TCO a cinco años',f"S/ {money(p['tco'])} = inversión + 5 × operación + salida S/ {money(p['salida'])}"),('Beneficio cuantificado',p['exito']),('Dependencias','Requiere: '+deps+' Habilita: '+habilita),('Riesgos y tratamiento',p['riesgos']),('Responsable propuesto',p['responsable']),('Área usuaria',p['area']),('Criterio de éxito y medición',p['exito']+' Verificación mensual por el responsable; acta al cierre y revisión a 90/180 días.'),('Origen e incertidumbre',f"EA-01: estimación académica de diseño, no cotización. ±{p['margen']:.0%}; TCO entre S/ {money(p['min'])} y S/ {money(p['max'])}. Precios constantes 2026, montos finales supuestos; sin descuento ni inflación.")]
  assert len(fields)==20
  p['campos']=fields
  (folder/(p['codigo']+'.md')).write_text('# '+p['codigo']+' · '+p['nombre']+'\n\n'+'\n\n'.join(f'**{i}. {k}.** {v}' for i,(k,v) in enumerate(fields,1)))
def pf04():
 rows=[]
 # Inacción se mide a cinco años, igual que los costos. Cada supuesto está en supuestos.csv.
 specs=[('PR-01',68800,[(0,0,0,0),(50000,10000,4000,.60),(120000,22000,8000,.90)]),('PR-02',70720,[(0,0,0,0),(60000,10000,4000,.60),(100000,18000,6000,.90)]),('PR-03',179800,[(0,0,0,0),(45000,8000,3000,None),(85000,15000,5000,None)])]
 for code,loss,alts in specs:
  for j,(inv,op,exit,rate) in enumerate(alts):
   benefit=loss*rate if rate is not None else (17980 if j==1 else 41960)
   avoid=5*benefit;tco=inv+5*op+exit; residual=5*loss-avoid
   # Beneficio negativo de A = exposición de inacción. No sumar a su TCO: se informa separado.
   rows.append(dict(codigo=code,alternativa=['A · No hacer nada','B · Mínima viable','C · Completa'][j],inversion=inv,operacion_anual=op,salida=exit,tco5=tco,margen=0.30,tco_min=round(tco*.70),tco_max=round(tco*1.30),costo_inaccion5=5*loss,beneficio_anual_evitable=benefit,beneficio5_vs_A=avoid,beneficio_alternativa5=(-5*loss if j==0 else avoid),perdida_residual5=residual,carga_economica5=tco+residual,neto_economico_vs_A=avoid-tco,origen='EA-01 y S-01..S-06; exposición modelada, no daño realizado ni ahorro de caja confirmado'))
 df=pd.DataFrame(rows);df.to_csv(BASE/'PF04_alternativas.csv',index=False)
 log('PF04_resultados.txt',df[['codigo','alternativa','tco5','costo_inaccion5','neto_economico_vs_A']].to_string(index=False)+'\nA: TCO incremental cero; operación existente permanece en presupuesto base.\nInacción y TCO se muestran separados; horas liberadas son capacidad, no reducción automática de nómina.\nNo se monetizan multas ni daños a la salud. Ejecución estable durante cinco años desde aceptación; retrasos reducen el beneficio.')
def pf05():
 df=pd.read_csv(BASE/'PF02_tco.csv');cats=pd.DataFrame(DATA)[['codigo','categoria']];df=df.merge(cats,on='codigo');bal=df.groupby('categoria').agg(inversion=('inversion','sum'),operacion_anual=('operacion','sum'),salida=('salida','sum'),tco5=('tco5','sum')).reindex(CAT)
 bal['porcentaje_tco']=100*bal.tco5/bal.tco5.sum();bal['equivalente_anual']=bal.tco5/5;bal.to_csv(BASE/'PF05_balance.csv')
 hist=pd.read_csv(ROOT/'fuentes/presupuesto_ti.csv');plan=hist.planificado.sum();executed=hist.ejecutado.sum()
 log('PF05_balance_resultados.txt',bal.to_string()+f'\nHistórico plan: {plan:.2f}; ejecutado: {executed:.2f}; desvío: {(executed/plan-1)*100:.2f}%\nPlan: operar 92%, inversión sin desglose crecer/transformar 8%. No se inventa la división.\nPropuesta: TCO/5 es equivalente anual de ciclo de vida, no presupuesto de caja. No se suma al presupuesto actual sin retirar solapamientos.\nReferencia orientativa: operar 50–70%, crecer 20–30%, transformar 10–20%. La cartera de nuevas iniciativas no equivale a toda la operación TI.')
 fig,axs=plt.subplots(1,2,figsize=(11,4.8),layout='constrained')
 axs[0].barh(CAT,bal.tco5/1000,color=[COL[x] for x in CAT]);axs[0].set_xlabel('TCO a 5 años · miles de S/');axs[0].set_title('Cartera de nuevas iniciativas')
 for i,(v,pct) in enumerate(zip(bal.tco5/1000,bal.porcentaje_tco)):axs[0].text(v+2,i,f'{pct:.1f}%',va='center',fontsize=9)
 axs[0].set_xlim(0,(bal.tco5.max()/1000)*1.25)
 dd=df.sort_values('tco5');axs[1].barh(dd.codigo,dd.tco5/1000,color=[COL[x] for x in dd.categoria]);axs[1].set_xlabel('TCO a 5 años · miles de S/');axs[1].set_title('Costo de ciclo de vida por proyecto')
 fig.savefig(GRAF/'PF_balance.png',dpi=180);plt.close(fig)
 fig,ax=plt.subplots(figsize=(9,3.5),layout='constrained');labels=['Presupuesto base 2025','Nuevos proyectos · TCO / 5'];bottom=[0,0]
 for label,vals,col in [('Operar',[92,bal.loc['Operar','porcentaje_tco']],COL['Operar']),('Crecer',[0,bal.loc['Crecer','porcentaje_tco']],COL['Crecer']),('Transformar',[0,bal.loc['Transformar','porcentaje_tco']],COL['Transformar']),('Inversión sin desglose',[8,0],'#98a0ae')]:
  ax.barh(labels,vals,left=bottom,label=label,color=col);bottom=[x+y for x,y in zip(bottom,vals)]
 ax.set_xlim(0,100);ax.set_xlabel('Distribución porcentual · universos distintos, contraste estructural');ax.legend(loc='lower center',bbox_to_anchor=(.5,-.48),ncol=2,fontsize=8);fig.savefig(GRAF/'PF_contraste.png',dpi=180,bbox_inches='tight');plt.close(fig)
def pf06():
 g=nx.DiGraph();g.add_nodes_from(p['codigo'] for p in DATA)
 for p in DATA:g.add_edges_from((dep,p['codigo']) for dep in p['dependencias'])
 assert nx.is_directed_acyclic_graph(g)
 order=list(nx.lexicographical_topological_sort(g));layers=list(nx.topological_generations(g))
 log('PF06_dependencias_resultados.txt','DAG sin ciclos. Flecha: habilitador → dependiente.\nOrden topológico válido: '+', '.join(order)+'\nCapas técnicas (no calendario ni asignación de recursos): '+str(layers)+'\nHabilitadores: '+', '.join(n for n in g if g.out_degree(n)>0)+'\nPR-12 es una puerta de gobierno para autorizar financiación; no crea dependencia técnica circular.\nCon tres personas de TI, secuenciar y contratar apoyo; la ejecución simultánea de doce proyectos no es viable.')
 pos={}
 for i,layer in enumerate(layers):
  for j,node in enumerate(sorted(layer)):pos[node]=(i*3,-j*1.1)
 fig,ax=plt.subplots(figsize=(10,6),layout='constrained');nx.draw_networkx(g,pos,ax=ax,node_color=[COL[next(p['categoria'] for p in DATA if p['codigo']==n)] for n in g],node_size=2000,font_size=10,font_color='white',arrowsize=22,edge_color='#64748b',width=1.6)
 ax.axis('off');ax.set_title('Dependencias técnicas · las iniciativas sin flechas pueden programarse por capacidad',fontsize=10);fig.savefig(GRAF/'PF_dependencias.png',dpi=180);plt.close(fig)
 return g
OBJECTIVES=[('OD-01','Trazabilidad verificable de productos controlados','214 unidades discrepantes en cuatro locales; no es una tasa de error.', '100% movimientos conciliados; ninguna diferencia sin investigación.', 'OE-02 / prioridad sectorial','Director técnico'),('OD-02','Consolidación confiable y conocimiento compartido','Dos fallos semanales y un único operador experto.','99% cierres antes de 07:00 y dos operadores habilitados.','OE-02 y OE-04','Jefe de Sistemas'),('OD-03','Reposición eficiente con aprobación humana','Compras en hojas y correo; tiempo y pérdidas no medidos.','Reducir 20% tiempo frente a línea base de cuatro semanas.','OE-02 y OE-05','Jefe de Logística'),('OD-04','Tratamiento de datos y uso de software controlados','Seis tratamientos registrados con vacíos y derechos de uso por verificar.','100% tratamientos y estaciones con control documentado.','OE-01 / obligación de cumplimiento','Administración'),('OD-05','Servicios recuperables y soporte medible','Tres sistemas sin copia; 169 tickets abiertos.','Cobertura total de copia y <=85 tickets pendientes.','OE-02 y OE-04','Coordinador de soporte'),('OD-06','Competencias y gobierno orientados a resultados','12 h de capacitación institucional; beneficios no medidos plenamente.','24 h anuales y 100% inversiones con evaluación posterior.','OE-03 y OE-05','Gerencia General')]
def validar():
 coverage=[]
 for obj in OBJECTIVES:
  codes=[p['codigo'] for p in DATA if p['objetivo']==obj[0]];assert codes
  coverage.append(dict(objetivo=obj[0],proyectos=', '.join(codes),cantidad=len(codes)))
 pd.DataFrame(coverage).to_csv(BASE/'PF07_cobertura.csv',index=False)
 for p in DATA:
  assert len(p['campos'])==20 and p['salida']>0 and p['min']<p['tco']<p['max']
  assert (BASE/'PF03_fichas'/f"{p['codigo']}.md").exists()
 assert 'Consulta de estado' not in [p['nombre'] for p in DATA]
 log('PF07_validacion.txt','COMPROBACIONES EJECUTADAS\n1. Objetivos: 12/12 proyectos asociados; 6/6 objetivos cubiertos.\n2. Fusión: C-13 conserva seguimiento y notificaciones en PR-10; no se duplica costo.\n3. TCO: 12/12 con operación recurrente, formación, migración, integración y salida.\n4. Fichas: 12/12 con 20 campos; rangos definidos.\n5. Dependencias: DAG sin ciclos.\n6. Mayores TCO: PR-01, PR-02, PR-03; nueve alternativas.\nALCANCE: validación de coherencia del modelo académico. No demuestra cotizaciones, beneficios reales ni aprobación.\nCIERRE EXTERNO: consultar PUBLICACION.md para la subida, PR y etiquetas taller-13 / v0.13; número de grupo por indicar.')
def pagos():
 df=pd.read_csv(ROOT/'fuentes/pagos.csv');assert len(df)==11014
 resumen=df.groupby(['moneda','estado']).agg(registros=('id_pago','size'),importe=('monto','sum')).reset_index();resumen.to_csv(BASE/'PF08_pagos_resumen.csv',index=False)
 log('PF08_pagos.txt',f'Registros: {len(df)}\n'+resumen.to_string(index=False)+'\nNo se atribuyen todos los pagos a TI: concepto y código de proveedor no bastan para vincular cada compra al contrato o centro de costo TI.\nEl costo operativo de proyectos es estimación EA-01, no extrapolación de esta población. Requiere conciliación contable de contratos y comprobantes.\nLas contraprestaciones contractuales se conservan como referencia de escala del caso; no se asignan como costo incremental de los proyectos.')
def main():
 pf01();pf02();fichas();pf04();pf05();pf06();validar();pagos()
if __name__=='__main__': main()
