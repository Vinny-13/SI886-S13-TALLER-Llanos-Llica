# Base analítica elaborada para Empresa 10

No es un PETI previo aprobado. Diagnóstico derivado de fuentes adjuntas; metas y códigos son propuestas.

| Origen | Brecha / estrategia | Sustento y decisión | Proyecto |
| --- | --- | --- | --- |
| 4.1.5 N-01 | Trazabilidad sectorial | 214 unidades discrepantes y retención de detalle de 90 días. El caso menciona exigencias de DIGEMID; su plazo exacto y admisión de libros electrónicos requieren validación sectorial. | PR-01 |
| 4.1.5 N-02 | Protección de datos | Seis tratamientos con vacíos; historial de medicamentos en marketing. Ley 29733 y reglamento como marco general; no se inventan multas ni plazos específicos. | PR-04 |
| 4.1.5 N-03 | Derechos de uso de software | Inventario con diferencias y etiquetas contradictorias. Verificar licencias y edición antes de imputar infracción o comprar. | PR-08 |
| 5.4.2 PT-01 | Integración confiable | Consolidación nocturna por archivos, dos fallos por semana y falta de soporte alterno. | PR-02 |
| 5.4.2 PT-02 | Control de identidades | Solo correo usa segundo factor y el POS no exige la política de contraseñas. | PR-09 |
| 4.3.5 BC-01 | Recuperación comprobada | Tres sistemas fuera de respaldos; no hay continuidad aprobada. Brecha de capacidad propuesta, sin asignar un nivel COBIT no medido. | PR-05 |
| 4.3.5 BC-02 | Medición de valor | Dos inversiones sin medición y una parcial; comité no activo. | PR-12 |
| 3.5 E-01 | DA: corregir compras con stock validado | Debilidad: compras por hojas y correo. Amenaza: exceso de compra y stock inconsistente. Respuesta: planificación sobre dato validado. | PR-03 |
| 3.5 E-02 | DA: reducir dependencia del experto | Debilidad: solo una persona reprocesa. Amenaza: indisponibilidad de esa persona. Respuesta: transferencia documentada. | PR-06 |
| 3.5 E-03 | DO: formación por rol | Debilidad: inducción desactualizada. Oportunidad: meta institucional de 24 h de capacitación. | PR-11 |
| 6.1.7 SD-01 | Servicio interno de soporte | Sin catálogo aprobado; 169 pendientes y registros incompletos. | PR-07 |
| 6.1.7 SD-02 | Servicio de derechos del cliente | No hay procedimiento para atender acceso o supresión de datos. Se propone un canal seguro sin ampliar uso de datos sensibles. | PR-10 |

Admisión: C-01..C-12 corresponden a PR-01..PR-12. C-13 «consulta de estado» se fusiona en PR-10 y conserva notificaciones y seguimiento. C-14 «asistente de recomendación de medicamentos» se retira por no tener fuente ni objetivo admisible. No queda costo duplicado por la fusión.


| Objetivo propuesto | Línea base / meta verificable | Vínculo institucional |
| --- | --- | --- |
| OD-01 · Trazabilidad verificable de productos controlados | 214 unidades discrepantes en cuatro locales; no es una tasa de error. Meta: 100% movimientos conciliados; ninguna diferencia sin investigación. | OE-02 / prioridad sectorial |
| OD-02 · Consolidación confiable y conocimiento compartido | Dos fallos semanales y un único operador experto. Meta: 99% cierres antes de 07:00 y dos operadores habilitados. | OE-02 y OE-04 |
| OD-03 · Reposición eficiente con aprobación humana | Compras en hojas y correo; tiempo y pérdidas no medidos. Meta: Reducir 20% tiempo frente a línea base de cuatro semanas. | OE-02 y OE-05 |
| OD-04 · Tratamiento de datos y uso de software controlados | Seis tratamientos registrados con vacíos y derechos de uso por verificar. Meta: 100% tratamientos y estaciones con control documentado. | OE-01 / obligación de cumplimiento |
| OD-05 · Servicios recuperables y soporte medible | Tres sistemas sin copia; 169 tickets abiertos. Meta: Cobertura total de copia y <=85 tickets pendientes. | OE-02 y OE-04 |
| OD-06 · Competencias y gobierno orientados a resultados | 12 h de capacitación institucional; beneficios no medidos plenamente. Meta: 24 h anuales y 100% inversiones con evaluación posterior. | OE-03 y OE-05 |

### Cartera depurada: códigos y trazabilidad

| Proyecto | Origen | Objetivo | Categoría |
| --- | --- | --- | --- |
| PR-01 · Trazabilidad de productos controlados | 4.1.5 N-01 | OD-01 | Transformar |
| PR-02 · Consolidación de stock tolerante a fallos | 5.4.2 PT-01 | OD-02 | Transformar |
| PR-03 · Reposición y distribución asistidas por demanda | 3.5 E-01 | OD-03 | Crecer |
| PR-04 · Protección de datos en fidelización y personal | 4.1.5 N-02 | OD-04 | Operar |
| PR-05 · Recuperación comprobada de sistemas críticos | 4.3.5 BC-01 | OD-05 | Operar |
| PR-06 · Transferencia de conocimiento del proceso nocturno | 3.5 E-02 | OD-02 | Operar |
| PR-07 · Mesa de servicio con catálogo y acuerdos medibles | 6.1.7 SD-01 | OD-05 | Operar |
| PR-08 · Inventario de software y regularización de uso | 4.1.5 N-03 | OD-04 | Operar |
| PR-09 · Ciclo de vida de accesos y cuentas privilegiadas | 5.4.2 PT-02 | OD-04 | Operar |
| PR-10 · Canal de ejercicio de derechos del cliente | 6.1.7 SD-02 | OD-04 | Crecer |
| PR-11 · Formación por rol en seguridad y dispensación digital | 3.5 E-03 | OD-06 | Operar |
| PR-12 · Control de inversiones y verificación de beneficios | 4.3.5 BC-02 | OD-06 | Operar |

Cobertura: OD-01 → PR-01; OD-02 → PR-02/06; OD-03 → PR-03; OD-04 → PR-04/08/09/10; OD-05 → PR-05/07; OD-06 → PR-11/12. Resultado: seis objetivos cubiertos. No se afirma cobertura de otros objetivos del PETI que no se hayan recibido.
