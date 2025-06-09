Tabla: Año Ficticio
| Columna | Tipo de Dato |
|---------|--------------|
| Año | int64 |

Tabla: Área Terapéutica
| Columna | Tipo de Dato |
|---------|--------------|
| IdAreaTerapeutica | string |
| Área Terapéutica | string |
| ImgAreaTerapeutica | string |
| Nombre Leading | string |
| Área Terapéutica BI |  |
| Área Terapéutica BI (KeyProduct) |  |
| Área Terapéutica BI (English) |  |

Tabla: Canal
| Columna | Tipo de Dato |
|---------|--------------|
| IdCanal | string |
| DescCanal | string |

Tabla: Cliente
| Columna | Tipo de Dato |
|---------|--------------|
| IdCategoria | string |
| Categoría | string |

Tabla: Compañia
| Columna | Tipo de Dato |
|---------|--------------|
| IdCompania | string |
| Compañía | string |

Tabla: Costo / Presupuesto
| Columna | Tipo de Dato |
|---------|--------------|
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
| Fecha |  |
| UNPresupuestada | double |
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
| CovidProduct | string |
| MLPresupuestadoAjustado | double |
| Trim | string |
| UNEstimadaBC | double |
| UNSTDEstimadaBC | double |
| MLEstimadoBC | double |
| USDEstimadoBC |  |
| MarcaBud | string |

Tabla: DimMarcaBudg
| Columna | Tipo de Dato |
|---------|--------------|
| MarcaBud | string |
| ATBudg | string |

Tabla: EstimadoPptoBudget
| Columna | Tipo de Dato |
|---------|--------------|
| IdCompania-IdProductoCompania | string |
| MarcaBud | string |
| ATBudg | string |
| Categoria | string |
| CUnitEstimado | double |
| CUnitPresupuestado | double |
| Cantidad | int64 |
| BusUnitBud | string |
| AnioEstimado | string |
| CostoEstimado | double |
| AnioPresupuesto | string |
| CostoPresupuesto | double |
| Origen | string |

Tabla: Fabricante
| Columna | Tipo de Dato |
|---------|--------------|
| IdFabricante | int64 |
| Descripcion | string |

Tabla: Familia
| Columna | Tipo de Dato |
|---------|--------------|
| IdFamilia | string |
| Familia | string |
| Nombre Leading Products | string |

Tabla: Forma Farmacéutica
| Columna | Tipo de Dato |
|---------|--------------|
| IdFormaFarmaceutica | string |
| Forma Farmacéutica | string |
| IdTipoForma | string |
| CantStandard | int64 |

Tabla: Key Product
| Columna | Tipo de Dato |
|---------|--------------|
| KeyProduct | string |

Tabla: Linea Comercial
| Columna | Tipo de Dato |
|---------|--------------|
| IdLinea | string |
| Línea Comercial | string |
| Laboratorio | string |

Tabla: Marca
| Columna | Tipo de Dato |
|---------|--------------|
| IdProducto | int64 |
| Marca | string |
| KeyProduct | string |
| Leading Brands | string |
| IdMarca | string |
| Marca (grupos) |  |

Tabla: País
| Columna | Tipo de Dato |
|---------|--------------|
| IdPais | string |
| DescPais | string |

Tabla: País / Zona-Gestión
| Columna | Tipo de Dato |
|---------|--------------|
| IdPais-IdZonaGestion | string |
| IdPais | string |
| DescripcionPais | string |
| IdZonaGestion | string |
| DescripcionZG |  |
| Zona Geográfica |  |
| IdTipoNegocio | string |
| IdTipoCrecimiento | string |
| TipoZonaGestion | string |
| Zona Geográfica (groups) |  |
| Img | string |
| Origen | string |
| DescripcionPaisIMS |  |
| Zona Reporte Mensual |  |
| DescripcionZG (Organic) |  |
| DescripcionZG (Mega Own Lines) |  |
| DescripcionZG (Exportaciones) |  |
| DescripcionZG (Mega Pharma) |  |
| DescripcionZG (Public Sales Ecuador) |  |
| Región |  |
| Grupo Gestiones | string |

Tabla: Período
| Columna | Tipo de Dato |
|---------|--------------|
| Anio | int64 |
| Mes | int64 |
| Fecha | dateTime |
| Quarter | int64 |

Tabla: Período a Analizar
| Columna | Tipo de Dato |
|---------|--------------|
| Año | int64 |
| Mes | int64 |
| Quarter | string |
| Fecha | dateTime |

Tabla: Periodos MAT
| Columna | Tipo de Dato |
|---------|--------------|
| Periodo | string |
| Fecha | dateTime |
| Fecha ultima | dateTime |
| Index | int64 |
| Real/Proy | string |
| Column6 | string |

Tabla: Producto MPh
| Columna | Tipo de Dato |
|---------|--------------|
| IdProductoMPh | int64 |
| Producto MPh | string |
| IdProductoFabricante | string |

Tabla: Producto Compañía
| Columna | Tipo de Dato |
|---------|--------------|
| IdProductoCompania | string |
| Presentación | string |
| FechaLanzamiento | dateTime |
| IdCompania | string |
| IdCompania-IdProductoCompania | string |
| Fecha | dateTime |
| FechaLanzamientoQuarter |  |

Tabla: SubFamilia
| Columna | Tipo de Dato |
|---------|--------------|
| IdProducto | int64 |
| Marca | string |
| SubFamilia | string |

Tabla: Target Product
| Columna | Tipo de Dato |
|---------|--------------|
| Target Product | string |

Tabla: Tipo de Producto
| Columna | Tipo de Dato |
|---------|--------------|
| IdTipoProducto | string |
| Descripcion | string |

Tabla: Ventas Mensuales
| Columna | Tipo de Dato |
|---------|--------------|
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
| Fecha |  dateTime|
| IdTipoNegocio | string |
| IdTipoProducto | string |
| IdFabricante | int64 |
| IdFormaFarmaceutica | string |
| ClasificacionOtcOtx | string |
| IdCompania-IdProductoCompania | string |
| IdPais-IdZonaGestion | string |
| IdCliente | string |
| Q | double |
| TargetProduct | string  |
| CovidProduct | string |
| CantidadElog | int64 |
| CostoConsolidadoUnitario | double |
| UnidadOtros | double |
| IdProductoFabricante | string |
| PharmaceuticalDivision | string |
| Marca Paragua | string |
| CategoriaFamilia | string |
| Idzonageografica | string |

Tabla: Zona-Gestión
| Columna | Tipo de Dato |
|---------|--------------|
| IdZonaGestion | string |
| Descripcion | string |
| IdTipoNegocio | string |
| IdTipoCrecimiento | string |
| TipoZonaGestion | string |