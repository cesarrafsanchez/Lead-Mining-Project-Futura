# Lead Enrichment System 🚀

## Descripción General

Lead Enrichment System es una plataforma de enriquecimiento de datos y segmentación comercial diseñada para transformar bases de datos empresariales crudas en listas de leads accionables para campañas de ventas outbound.

El objetivo principal del sistema es procesar grandes volúmenes de registros RUC (RUC 10 y RUC 20), enriquecerlos con información de identidad y telecomunicaciones, validar números telefónicos y generar archivos Excel optimizados para el equipo comercial.

El proyecto está enfocado en:

- Extraer DNIs desde RUCs
- Identificar representantes legales desde SUNAT
- Obtener números telefónicos desde TACTO
- Validar líneas mediante OSIPTEL
- Segmentar leads por distrito y criterios comerciales
- Priorizar leads para campañas de ventas

---

# Objetivo de Negocio

El sistema busca entregar al equipo comercial:

✅ Bases de datos limpias  
✅ Números telefónicos validados  
✅ Segmentación por distritos  
✅ Priorización comercial  
✅ Archivos Excel listos para llamar  

Esto permitirá que las campañas comerciales sean:

- Más directas
- Más medibles
- Más eficientes
- Más enfocadas en conversión

---

# Flujo Principal del Sistema

```text
BASE DE DATOS CRUDA (RUCs)
                │
                ▼
PREPROCESAMIENTO
(Separación RUC10 / RUC20)
                │
                ▼
EXTRACCIÓN DE DNI
                │
                ▼
CONSULTA SUNAT
(Representantes legales)
                │
                ▼
CONSULTA TACTO
(Obtención de teléfonos)
                │
                ▼
VALIDACIÓN OSIPTEL
(Operador y consistencia)
                │
                ▼
SCORING Y SEGMENTACIÓN
                │
                ▼
EXPORTACIÓN EXCEL FINAL
```

---

# Alcance del MVP

La primera versión del sistema estará enfocada únicamente en:

- Procesamiento de datos
- Enriquecimiento de información
- Obtención de teléfonos
- Validación de líneas
- Exportación comercial

NO se incluirá en esta etapa:

- Frontend
- Dashboards
- APIs
- Automatización de campañas
- Integraciones CRM
- Machine Learning

Estas funcionalidades serán consideradas en futuras iteraciones.

---

# Funcionalidades Principales

## 1. Procesamiento de RUCs

### RUC 10
- Extracción directa del DNI
- Normalización de datos
- Segmentación por distrito

### RUC 20
- Consulta automática a SUNAT
- Obtención de representantes legales
- Extracción de DNI del representante

---

## 2. Enriquecimiento con TACTO

- Inicio de sesión automatizado
- Búsqueda por DNI
- Extracción de teléfonos
- Normalización de números
- Eliminación de duplicados

---

## 3. Validación con OSIPTEL

- Validación de operador
- Verificación de consistencia
- Incremento de confianza del lead

---

## 4. Segmentación Comercial

El sistema segmentará los leads por:

- Distrito
- Tipo de lead
- Operador
- Score de confianza
- Prioridad comercial

---

## 5. Motor de Scoring

Cada lead recibirá un score basado en:

| Factor | Peso |
|---|---|
| Línea validada | Alto |
| Operador Claro | Alto |
| Línea móvil | Medio |
| Consistencia entre fuentes | Alto |
| Probabilidad de línea activa | Medio |

Esto permitirá priorizar los mejores leads para las campañas comerciales.

---

# Resultado Final Esperado

El sistema generará un archivo Excel final con:

| Campo | Descripción |
|---|---|
| DNI | Identidad del lead |
| Nombre Completo | Nombre de la persona |
| Distrito | Segmentación comercial |
| Teléfono | Número validado |
| Operador | Operador telefónico |
| Tipo Lead | RUC10 / RUC20 |
| Score | Nivel de confianza |
| Prioridad | HOT / WARM / COLD |

---

# Estructura Propuesta del Proyecto

```text

├── data/
│   ├── inputs/
│   ├── outputs/
│   ├── temp/
│   └── logs/
│
├── preprocessing/
│   ├── split_rucs.py
│   ├── dni_extractor.py
│   ├── district_classifier.py
│   └── cleaner.py
│
├── sunat/
│   ├── sunat_scraper.py
│   ├── representative_parser.py
│   └── captcha_handler.py
│
├── tacto/
│   ├── tacto_scraper.py
│   ├── session_manager.py
│   └── phone_parser.py
│
├── validation/
│   ├── osiptel_validator.py
│   └── phone_cleaner.py
│
├── exports/
│   └── excel_exporter.py
│
├── shared/
│   ├── base_scraper.py
│   ├── logger.py
│   ├── utils.py
│   └── config.py
│
├── tests/
│
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
└── README.md
```

---

# Tecnologías del Proyecto

| Tecnología | Uso |
|---|---|
| Python | Lenguaje principal |
| Playwright | Automatización web |
| Pandas | Procesamiento de datos |
| SQLite | Persistencia local |
| Docker | Contenerización |
| OpenPyXL | Exportación Excel |
| Logging | Monitoreo y debugging |

---

# Principios de Arquitectura

El proyecto seguirá los siguientes principios:

- Arquitectura modular
- Separación de responsabilidades
- Pipeline escalable
- Persistencia inmediata
- Automatización resiliente
- Enfoque comercial

---

# Estrategia de Datos

## Segmentación por Distritos

Los leads serán agrupados por distrito para medir:

- Conversión comercial
- Rendimiento de campañas
- Performance por zona

Esto permitirá optimizar campañas futuras basadas en resultados reales.

---

## Priorización Comercial

El sistema priorizará:

- Líneas de alta confianza
- Líneas activas
- Leads compatibles con Claro
- Prospectos de alta probabilidad

---

# Roadmap del Proyecto

## Fase 1 — MVP
- Configuración del repositorio
- Arquitectura inicial
- Preprocesamiento RUC
- Integración SUNAT
- Integración TACTO
- Validación OSIPTEL
- Exportación Excel

---

## Fase 2 — Optimización
- Procesamiento concurrente
- Sistema de retries
- Mejor scoring
- Rotación de proxies
- Optimización de rendimiento

---

## Fase 3 — Inteligencia Comercial
- Dashboards
- Analítica de campañas
- Integración CRM
- Automatización outbound
- Scoring predictivo

---

# Organización del Proyecto en ClickUp

La gestión del proyecto estará dividida en:

```text
1. Gestión y Arquitectura
2. Infraestructura y Setup
3. Preprocesamiento de Datos
4. Integración SUNAT
5. Integración TACTO
6. Validación Telefónica
7. Motor de Scoring
8. Exportación Comercial
9. QA y Testing
10. Despliegue y Operaciones
11. Mejoras Futuras
```

---

# Milestones

## Milestone 1
Pipeline RUC funcional

## Milestone 2
Extracción masiva TACTO funcional

## Milestone 3
Validación OSIPTEL integrada

## Milestone 4
Primer Excel comercial entregado

---

# Métricas de Éxito

El éxito del sistema será medido por:

- Cantidad de leads enriquecidos
- Tasa de validación telefónica
- Conversión comercial por distrito
- Rendimiento de campañas
- Throughput operativo

---

# Visión Futura

La visión a largo plazo es evolucionar el proyecto hacia un:

> Motor de Inteligencia Comercial y Priorización de Leads

Capacidades futuras:

- Integración CRM
- Automatización de campañas
- Integración WhatsApp
- IA para scoring predictivo
- Analítica comercial
- Dashboards en tiempo real

---

# Estado Actual del Proyecto

```text
Fase Actual: Planificación y Arquitectura
Estado: En Desarrollo
```

---

# Notas Importantes

Actualmente el proyecto está enfocado en:

- Entrega rápida del MVP
- Utilidad comercial inmediata
- Calidad de datos
- Escalabilidad operativa

La prioridad principal es generar bases de datos comerciales listas para campañas de ventas lo más rápido posible.