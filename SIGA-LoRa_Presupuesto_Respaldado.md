# Presupuesto Técnico Respaldado — Proyecto SIGA-LoRa

**Proyecto:** SIGA-LoRa: Sistema Inteligente de Gestión de Alertas  
**Subtítulo:** Prototipo de monitoreo inalámbrico de niveles de agua ante riesgos de inundación  
**Institución:** Universidad Dr. Andrés Bello (UNAB) — Facultad de Tecnología e Innovación  
**Asignatura:** Sistemas Digitales  
**Catedrático:** MduEV. Ing. Franklin Geovany Buruca Hernández  
**Fecha de consolidación:** San Miguel, sábado 10 de octubre de 2026  

---

## 1. Resumen Ejecutivo del Presupuesto

El presupuesto del proyecto se encuentra estructurado en dos categorías claramente delimitadas:
1. **Componentes y equipos disponibles:** Hardware adquirido previamente por el equipo de trabajo en plataformas de importación directa (AliExpress), cuyo valor se consigna con fines de auditoría e inventario académico.
2. **Materiales y componentes por adquirir:** Sensores, circuitos integrados lógicos discretos (familia 74HC), interfaces de señalización, placas de circuito perforadas para soldadura manual, consumibles de montaje y elementos de maquetado.

| Categoría | Subtotal Calculado (USD) | Estado Contable |
|---|---:|---|
| **A. Equipos y Módulos Disponibles en Inventario** | **$39.90** | Adquirido previamente |
| **B. Materiales, Sensores y Componentes por Adquirir** | **$48.34** | Proyectado / Pendiente de compra |
| **COSTO TOTAL REFERENCIAL DEL PROYECTO** | **$88.24** | Inversión Global Referencial |

---

## 2. Desglose Detallado de Materiales y Cotizaciones

### Categoría A: Equipos y Módulos de Adquisición y Comunicaciones (Disponibles)

| Ítem | Cant. | Componente / Descripción Técnica | Función en el Proyecto | Proveedor / Referencia | P. Unit. (USD) | Subtotal (USD) | Estado y Observaciones Técnicas |
|:---:|:---:|---|---|---|---:|---:|---|
| A.1 | 1 | **Arduino Uno R3** (Microcontrolador ATmega328P, 16 MHz, 5V) | Adquisición de señales analógicas/digitales y lógica de control primario en Estación A. | AliExpress (precio referencial de importación) | $5.10 | $5.10 | **Disponible.** Unidad física en poder del equipo. Se dispone adicionalmente de un Arduino Nano en reserva sin costo imputado. |
| A.2 | 2 | **Módulo ESP32 NodeMCU** (SoC dual-core Xtensa, 30 pines, 3.3V) | Gestión de capa física/enlace de comunicación LoRa y control de paquetes en Estación A (Tx) y Estación B (Rx). | AliExpress (precio referencial de importación) | $4.37 | $8.74 | **Disponibles.** 2 unidades en poder del equipo. Trabajan a niveles lógicos de 3.3V. |
| A.3 | 2 | **HopeRF RFM95W 915 MHz** (Módulo transceptor LoRa SX1276) | Enlace inalámbrico de telemetría a larga distancia sin dependencia de redes celulares o Wi-Fi. Incluye antena helicoidal básica. | Paquete importado por el equipo | $7.70 | $15.40 | **Disponibles.** Sintonizados a la banda ISM regional de 915 MHz. Requieren verificar soldadura del conector/antena. |
| A.4 | 2 | **Antenas LoRa omnidireccionales de 6 dBi** (868/915 MHz) con cable pigtail adaptador U.FL/IPEX1 a SMA hembra | Radiación y recepción optimizada de señales de radiofrecuencia para maximizar el margen de enlace. | Paquete importado por el equipo | $5.33 | $10.66 | **Disponibles.** Producto externo e independiente de la antena helicoidal incluida en el módulo RFM95W. |
| **SUBTOTAL A** | **7** | \multicolumn{3}{l|}{**Subtotal Componentes Disponibles (Valor referencial inventario)**} | --- | **$39.90** | **Total inventariado** |

---

### Categoría B: Sensores, Lógica Digital Discreta, Actuadores y Montaje (Por Adquirir)

| Ítem | Cant. | Componente / Descripción Técnica | Función en el Proyecto | Proveedor / Referencia de Cotización | P. Unit. (USD) | Subtotal (USD) | Estado y Observaciones de Compra |
|:---:|:---:|---|---|---|---:|---:|---|
| B.1 | 1 | **Sensor ultrasónico impermeable JSN-SR04T** (Transductor sellado con cable de 2.5 m) | Medición continua sin contacto de la distancia a la lámina de agua en el cauce/canal. | Estimación referencial comercial | $2.12 | $2.12 | **Por adquirir.** Estimación de borrador. Requiere cotización o confirmación en plaza local. |
| B.2 | 3 | **Interruptores de nivel tipo flotador vertical** (Contactos secos magnéticos Reed switch) | Detección física discreta escalonada de umbrales críticos ($L_1$, $L_2$, $L_3$). | Estimación referencial comercial | $1.29 | $3.87 | **Por adquirir.** 3 unidades para validación combinacional redundante ante fallas del ultrasónico. |
| B.3 | 1 | **CI 74HC08** (4 compuertas AND de 2 entradas, encapsulado DIP-14) | Validación lógica cableada de condiciones de alarma simultáneas (lógica combinacional pura). | [LCSC C2887 (Texas Instruments)](https://www.lcsc.com/product-detail/C2887.html) | $0.83 | $0.83 | **Por adquirir.** Familia CMOS de alta velocidad compatible con 3.3V–5V. No sustituir por 74LS sin verificar niveles. |
| B.4 | 1 | **CI 74HC32** (4 compuertas OR de 2 entradas, encapsulado DIP-14) | Enrutamiento combinacional de señales de advertencia física hacia líneas de interrupción. | [LCSC C2894 (Texas Instruments)](https://www.lcsc.com/product-detail/C2894.html) | $0.73 | $0.73 | **Por adquirir.** Compatible pin a pin en baquela perforada. |
| B.5 | 1 | **CI 74HC04N** (6 inversores NOT, encapsulado DIP-14) | Inversión de niveles lógicos provenientes de flotadores normalmente cerrados. | [LCSC C669327 (HTC)](https://www.lcsc.com/es/product-detail/C669327.html) | $1.92 *(lote 5)* | $1.92 | **Por adquirir.** Proveedor exige lote mínimo de 5 uds ($1.92 el lote). Se instala 1 unidad y 4 quedan en reserva técnica. |
| B.6 | 1 | **CI 74HC238N** (Decodificador / Demultiplexor 3 a 8 líneas, salidas activas en alto, DIP-16) | Decodificación física del código binario recibido en Estación B para excitar canales de señalización de manera mutuamente excluyente. | [LCSC C5310756 (HGSEMI)](https://www.lcsc.com/product-detail/C5310756.html) / [TI CD74HC238](https://www.ti.com/product/CD74HC238) | $1.12 *(lote 5)* | $1.12 | **Por adquirir.** Proveedor exige lote mínimo de 5 uds ($1.12 el lote). Se instala 1 unidad y 4 quedan en reserva técnica. |
| B.7 | 4 | **Diodos LED de 5 mm** (1 verde, 1 amarillo, 1 naranja, 1 rojo) | Señalización visual local por código de alerta en el panel receptor comunitario. | [Steren Optoelectrónica](https://www.steren.com.sv/proyectos-de-electronica/optoelectronica) | $0.20 | $0.80 | **Por adquirir.** Precios de catálogo local en Steren El Salvador ($0.20 c/u). Desglosados individualmente. |
| B.8 | 1 | **Mini buzzer piezoeléctrico continuo BGD08** (5V DC) | Alerta sonora audible local activada exclusivamente ante el nivel de peligro crítico. | [Steren Zumbadores](https://www.steren.com.sv/proyectos-de-electronica/buzzers-zumbadores) | $1.00 | $1.00 | **Por adquirir.** Precio de catálogo Steren El Salvador. |
| B.9 | 2 | **Baquelas perforadas soldables mod. 400** (Disposición de pistas tipo protoboard, fibra/fenólica) | Soporte físico soldado para el montaje definitivo de microcontroladores y circuitos de radio en ambas estaciones. | [Steren Baquelas](https://www.steren.com.sv/proyectos-de-electronica/baquelas-y-accesorios-de-c-i) | $3.49 | $6.98 | **Por adquirir.** No son protoboards sin soldadura; son placas soldables con pistas preformadas para garantizar un acabado profesional y permanente. |
| B.10 | 2 | **Baquelas perforadas soldables mod. 405** (Islas de cobre individuales para soldadura de CI) | Soporte físico soldado para las etapas lógicas discretas (compuertas 74HC y DEMUX). | [Steren Baquelas](https://www.steren.com.sv/proyectos-de-electronica/baquelas-y-accesorios-de-c-i) | $1.49 | $2.98 | **Por adquirir.** Facilita el cableado punto a punto con alambre estañado. |
| B.11 | 1 | **Soldadura estaño-plomo SOL60-020** (Tubo dispensador de 17 gramos, aleación 60/40 con núcleo de resina) | Fijación mecánica y unión eléctrica permanente de componentes en baquelas perforadas. | [Steren Cautines y Soldadura](https://www.steren.com.sv/herramientas/cautines-y-accesorios) | $3.99 | $3.99 | **Por adquirir.** Consumible indispensable para cumplir con la rúbrica de ensamblado físico sin protoboard a presión. |
| B.12 | 8 m | **Alambre estañado para conexiones 22 AWG** (Aislamiento PVC flexible) | Puentes de interconexión y ruteo punto a punto sobre pistas de baquela perforada. | [Steren Alambre 22 AWG](https://www.steren.com.sv/alambre-esta-ado-para-conexiones-22-awg-color-negro.html) | $0.25 / m | $2.00 | **Por adquirir.** 8 metros calculados para el ruteo interno de ambas estaciones ($2.00 total). |
| B.13 | Lote | **Zócalos DIP (14 y 16 pines), resistencias de polarización (220/330 $\Omega$) y capacitores de desacoplo (0.1 $\mu$F cerámicos)** | Protección térmica de circuitos integrados durante soldadura, limitación de corriente para LEDs y filtrado de ruido en líneas de alimentación. | Electrónica 2001 / Steren El Salvador (estimado de plaza) | $3.50 | $3.50 | **Por adquirir.** Estimación referencial de lote pasivo. Evita dañar los CI por sobrecalentamiento directo al soldar. |
| B.14 | 2 | **Convertidores de nivel lógico bidireccionales 3.3V $\leftrightarrow$ 5V** (4 canales con MOSFET BSS138) | Adaptación de niveles de tensión entre las líneas UART/SPI de Arduino Uno (5V) y los módulos ESP32 / LoRa RFM95W (3.3V). | Mercado local de electrónica (San Miguel / San Salvador) | $1.25 | $2.50 | **Por adquirir.** Esencial para evitar la degradación o destrucción por sobretensión de las entradas del ESP32 y transceptor LoRa. |
| B.15 | Lote | **Accesorios de alimentación y cableado** (Portapilas 18650/AA, cables USB de prueba, borneras de conexión a tornillo) | Suministro de energía eléctrica regulada e independiente para el nodo sensor Tx y el nodo receptor Rx. | Comercio local / Steren | $6.00 | $6.00 | **Por adquirir.** Estimación referencial para pruebas autónomas de laboratorio. |
| B.16 | Lote | **Materiales de maquetado y soporte estructural** (Cortes de acrílico/madera MDF, tornillería plástica M3, canal de prueba a escala) | Construcción de la maqueta física a escala del cauce/tanque de monitoreo para la defensa en vivo. | Ferretería local / librería técnica | $8.00 | $8.00 | **Por adquirir.** Exigencia de la guía académica institucional para demostración funcional. |
| **SUBTOTAL B** | **---** | \multicolumn{3}{l|}{**Subtotal Materiales por Adquirir (Costo proyectado de compra)**} | --- | **$48.34** | **Total compras pendientes** |
| **TOTAL GENERAL** | **---** | \multicolumn{3}{l|}{**COSTO TOTAL ESTIMADO REFERENCIAL DEL PROYECTO (A + B)**} | --- | **$88.24** | **Presupuesto Consolidado** |

---

## 3. Justificación Técnica de Diferencias y Decisiones de Compra

1. **Aclaración de antenas LoRa y módulos RFM95W:**
   - La inspección física del paquete adquirido confirmó que cada módulo HopeRF RFM95W ($7.70 c/u) incluye una pequeña antena helicoidal de resorte de baja ganancia (~2 dBi).
   - Las antenas omnidireccionales de 6 dBi ($5.33 c/u) con conector SMA y cable pigtail U.FL/IPEX son componentes externos adquiridos para mejorar la sensibilidad y el alcance del prototipo. Por tal motivo, se presentan en filas rigurosamente separadas.
2. **Familia 74HC vs 74LS:**
   - Se seleccionaron circuitos integrados de la familia **74HC** (CMOS de alta velocidad: 74HC08, 74HC32, 74HC04, 74HC238) debido a su amplio rango de alimentación (2V a 6V), compatibilidad directa con voltajes de 3.3V y mínimo consumo de corriente estática.
   - Aunque Steren El Salvador comercializa chips TTL de la serie 74LS (ej. SN74LS08N a $0.80, SN74LS32N a $0.75), estos operan estrictamente a 5V $\pm 5\%$, consumen mayor corriente y se encuentran frecuentemente agotados en línea. No deben reemplazarse sin una adaptación de niveles explícita.
3. **Placas perforadas soldables (Modelos 400 y 405 de Steren):**
   - El docente prohíbe el uso de protoboards de inserción a presión en el entregable final.
   - El modelo 400 ($3.49) posee una matriz de perforaciones con pistas de cobre interconectadas idéntica al layout de una protoboard, lo que agiliza el cableado de microcontroladores manteniendo la soldadura física definitiva.
   - El modelo 405 ($1.49) posee islas de soldadura individuales, ideal para circuitería lógica compacta y desacoplo de ruido.
4. **Lotes mínimos de compra vs. componentes instalados:**
   - Los distribuidores industriales internacionales (como LCSC) imponen compras mínimas de 5 unidades para chips económicos como el 74HC04 ($1.92 por 5 uds) y el 74HC238 ($1.12 por 5 uds). En el presupuesto se registra el costo íntegro del paquete necesario para la adquisición, aclarando que las unidades sobrantes forman parte de la reserva técnica ante contingencias de laboratorio.

