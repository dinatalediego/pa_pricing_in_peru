# Methodology Playbook

## Principio

La tesis debe separar tres preguntas:

1. **Descripción:** ¿qué pasó?
2. **Predicción:** ¿qué probablemente pasará?
3. **Causalidad/decisión:** ¿qué cambia si modifico X?

La tercera es la más valiosa para el tema principal.

## Pricing inmobiliario

### Baseline panel
`log(outcome_it) = beta * log(price_it) + unit/project FE + time FE + controls + error_it`

Riesgo: el precio es endógeno; una inmobiliaria baja precios cuando anticipa baja demanda.

### Estrategias mejores

#### Event study
Usar cambios discretos/estandarizados de pricing y observar trayectoria de:
- hazard;
- leads;
- separaciones;
- absorción.

Validar pre-trends.

#### Difference-in-differences
Si un cambio afecta ciertas tipologías/proyectos y otros comparables no.

#### Instrumental variables
Solo con instrumento defendible: regla de pricing, hito administrativo o shock de costo que afecte precio pero no demanda directamente, sujeto a discusión rigurosa.

#### Survival analysis
Outcome natural: tiempo hasta venta.
Modelos:
- Kaplan–Meier descriptivo;
- Cox PH;
- Accelerated Failure Time;
- discrete-time hazard con panel mensual/semanal.

Tratar cambios de precio como covariables time-varying.

#### Heterogeneidad
- interacciones económicas pre-especificadas;
- causal forests / generalized random forests como complemento;
- no usar SHAP como sustituto de identificación causal.

## Pass-through

Modelos:
- local projections;
- distributed lags;
- panel LP con FE;
- ARDL/ECM para series/panel cuando haya cointegración;
- respuestas asimétricas a apreciación/depreciación.

Outcomes inmobiliarios:
- precio lista;
- descuento;
- precio final;
- absorción.

## Market heat

Inspiración estructural:
list price + sale price + time-on-market + stock.

Versión inicial:
- índices estandarizados;
- PCA/factor dinámico para descriptivo;
- modelo estructural de search/bargaining para contribución fuerte.

## Infraestructura

Preferencia:
- event study DiD;
- distancia continua/rings;
- controles espaciales;
- cluster de errores;
- placebo stations/dates;
- spillovers explícitos.

## Combustibles

- spatial lags/reaction functions;
- station FE + time FE;
- pass-through distributed lag;
- asymmetric error correction;
- HHI/local competitor density;
- screenings de dispersión/sincronización como alertas, nunca como prueba suficiente de colusión.

## ML

Usarlo para:
- benchmark predictivo;
- nonlinearities;
- heterogeneidad;
- uplift/policy learning exploratorio.

No usarlo para afirmar causalidad por feature importance.

## Robustness mínimo

- definiciones alternativas de outcome;
- winsorization documentada;
- distintos FE;
- lags/leads;
- placebo;
- ventanas alternativas;
- clustering adecuado;
- split temporal para modelos predictivos;
- reproducibilidad mediante seed/config.
