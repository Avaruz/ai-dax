# Modelo de Datos (Extraído de TDML)

## Tabla: Año Ficticio

| Columna | Tipo de Dato |
|---------|---------------|
| Año | int64 |

## Tabla: Área Terapéutica

| Columna | Tipo de Dato |
|---------|---------------|
| IdAreaTerapeutica | string |
| Área Terapéutica | string |
| ImgAreaTerapeutica | string |
| Nombre Leading | string |

## Tabla: Costo / Presupuesto

| Columna | Tipo de Dato |
|---------|---------------|
| IdPeriodo | string |
| IdCompania-IdProductoCompania | string |
| IdProductoCompania | string |
| IdCompania | string |
| IdCanal | string |
| IdProducto | int64 |
| IdLinea | string |
| IdFamilia | string |
| IdAreaTerapeutica | string |
| IdIndicacion | string |
| IdPais | string |
| IdPais-IdZonaGestion | string |
| IdProductoMPh | int64 |
| IdZonaGestion | string |
| IdTipoNegocio | string |
| IdTipoProducto | string |
| IdFabricante | int64 |
| IdFormaFarmaceutica | string |
| ClasificacionOtcOtx | string |
| CostoConsolidado | double |
| CostoConsolidadoUnitario | double |
| FechaCostoConsolidado | int64 |
| Fecha  | double |
| UNEstimada | double |
| UNSTDPresupuestada | double |
| UNSTDEstimada | double |
| MLPresupuestado | double |
| MLEstimado | double |
| USDPresupuestado | double |
| USDEstimado | double |
| UNEstimadaMLB | double |
| UNSTDEstimadaMLB | double |
| MLEstimadoMLB | double |
| USDEstimadoMLB | double |
| QPresupuestado | double |
| QEstimado | double |
| TargetPRoduct | string |
| IdMarca  | string |
| MLPresupuestadoAjustado | double |
| Trim | string |
| UNEstimadaBC | double |
| UNSTDEstimadaBC | double |
| MLEstimadoBC | double |
| USDEstimadoBC | double |
| ConcatPaisMarca  | string |

## Tabla: Forma Farmacéutica

| Columna | Tipo de Dato |
|---------|---------------|
| IdFormaFarmaceutica | string |
| Forma Farmacéutica | string |
| IdTipoForma | string |
| CantStandard | int64 |

## Tabla: Key Product

| Columna | Tipo de Dato |
|---------|---------------|
| KeyProduct | string |

## Tabla: Linea Comercial

| Columna | Tipo de Dato |
|---------|---------------|
| IdLinea | string |
| Línea Comercial | string |
| Laboratorio | string |

## Tabla: País / Zona-Gestión

| Columna | Tipo de Dato |
|---------|---------------|
| IdPais-IdZonaGestion | string |
| IdPais | string |
| DescripcionPais | string |
| IdZonaGestion | string |
| DescripcionZG | string |
| Zona  | string |
| IdTipoCrecimiento | string |
| TipoZonaGestion | string |
| Zona Geográfica (groups)'  | string |
| Origen | string |
| DescripcionPaisIMS  | string |

## Tabla: Período a Analizar

| Columna | Tipo de Dato |
|---------|---------------|

## Tabla: Periodos MAT

| Columna | Tipo de Dato |
|---------|---------------|
| Periodo | string |
| Fecha | dateTime |
| Fecha ultima | dateTime |
| Fecha corta'  | int64 |
| Real/Proy | string |
| Column6 | string |

## Tabla: Producto MPh

| Columna | Tipo de Dato |
|---------|---------------|
| IdProductoMPh | int64 |
| Producto MPh | string |
| IdProductoFabricante | string |

## Tabla: Producto Compañía

| Columna | Tipo de Dato |
|---------|---------------|
| IdProductoCompania | string |
| Presentación | string |
| FechaLanzamiento | dateTime |
| Año  | string |
| IdCompania-IdProductoCompania | string |

## Tabla: Target Product

| Columna | Tipo de Dato |
|---------|---------------|
| Target Product | string |

## Tabla: Tipo de Producto

| Columna | Tipo de Dato |
|---------|---------------|
| IdTipoProducto | string |
| Descripcion | string |

## Tabla: Ventas Mensuales

| Columna | Tipo de Dato |
|---------|---------------|
| IdPeriodo | string |
| IdProductoCompania | string |
| IdCompania | string |
| IdCanal | string |
| IdProducto | int64 |
| IdLinea | string |
| IdFamilia | string |
| IdAreaTerapeutica | string |
| IdIndicacion | string |
| IdPais | string |
| IdProductoMPh | int64 |
| IdZonaGestion | string |
| UN | double |
| UNSTD | double |
| ML | double |
| USD | double |
| Fecha  | string |
| IdTipoProducto | string |
| IdFabricante | int64 |
| IdFormaFarmaceutica | string |
| ClasificacionOtcOtx | string |
| IdCompania-IdProductoCompania | string |
| IdPais-IdZonaGestion | string |
| IdCliente | string |
| Old IDCompañia'  | double |
| AreaT English'  | string |
| Leading Brands'  | string |
| CantidadElog | int64 |
| CostoConsolidadoUnitario | double |
| UnidadOtros | double |
| ConcatPaisMarca  | string |
| PharmaceuticalDivision | string |
| Marca Paragua | string |
| CategoriaFamilia | string |
| Idzonageografica | string |

