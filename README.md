# Taller 13 · Llanos-Llica

**SI-886 · Planeamiento Estratégico de TI · Universidad Privada de Tacna**

Empresa 10: **Cadena de Farmacias Buena Salud E.I.R.L.**, organización ficticia del banco del curso.

Equipo: **Llanos-Llica**. Datos personales consignados: Vincenzo Rafael Llanos Niño · 2023076796. No se inventa el nombre completo ni código del compañero.

## Documentos

- [Informe PDF · 38 páginas](SI886-S13-TALLER-Llanos-Llica.pdf)
- [Word editable](SI886-S13-TALLER-Llanos-Llica.docx)
- [Excel con fórmulas](Anexo_A_Portafolio_y_TCO.xlsx)
- [Informe completo en Markdown](Informe_completo.md)
- [Sección 7.1 del PETI](07_portafolio/7.1_Portafolio_de_Proyectos.md)
- [Doce fichas de veinte campos](07_portafolio/PF03_fichas/)
- [Registro de evidencia y enlaces por resultado](evidencias/S13/registro_evidencias.csv)
- [Estado de publicación y cierre](PUBLICACION.md)

## Resultados y evidencia

| Artefacto | Contenido |
|---|---|
| [Admisión](07_portafolio/PF00_admision.csv) | 14 candidatos, 12 admitidos, una fusión y un retiro |
| [Cartera](07_portafolio/PF01_portafolio_candidatos.csv) | Cinco fuentes admisibles y objetivos trazables |
| [TCO](07_portafolio/PF02_tco.csv) | Inversión, operación, salida, rango y factor por proyecto |
| [Alternativas](07_portafolio/PF04_alternativas.csv) | Tres casos de negocio y nueve escenarios |
| [Balance](07_portafolio/graficos/PF_balance.png) | Categorías y costo por proyecto |
| [Dependencias](07_portafolio/graficos/PF_dependencias.png) | DAG, habilitadores y orden de implementación |
| [Cobertura](07_portafolio/PF07_cobertura.csv) | Seis objetivos propuestos cubiertos |
| [Sostenibilidad](07_portafolio/PF09_sostenibilidad.csv) | Cinco dimensiones para doce proyectos |
| [Supuestos](07_portafolio/supuestos.csv) | Separación entre hechos y estimaciones académicas |
| [Salidas de ejecución](evidencias/S13/salidas/) | Cálculos y validaciones reproducibles |
| [Fuentes](fuentes/procedencia.json) | URL y commit de los archivos del banco docente |

Inversión inicial modelada: **S/ 572 000**. TCO a cinco años: **S/ 1 145 000**, con operación y salida. Los costos y eficacias son estimaciones académicas, no cotizaciones ni resultados reales.

## Reproducir

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python 07_portafolio/modelo_s13.py
```

En Windows: `.venv\Scripts\python` y `.venv\Scripts\pip`. Ver [LEEME](LEEME.md) para alcance y dependencias.

## Alcance académico

La base analítica previa se elaboró desde los archivos del caso y debe armonizarse con el PETI del equipo. El número de grupo no fue indicado. La publicación, las ramas, las etiquetas y el PR deben verificarse con el estado registrado en PUBLICACION.md; su sola mención no demuestra que existan.
