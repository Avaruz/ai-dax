# Documentación del Modelo de Datos

Tabla: Año Ficticio
------------------------------
- Año (int64)

Tabla: Área Terapéutica
------------------------------
- IdAreaTerapeutica (string)
- Área Terapéutica (string)
- ImgAreaTerapeutica (string)
- Nombre Leading (string)
- Área Terapéutica BI
- Área Terapéutica BI (KeyProduct)
- Área Terapéutica BI (English)

Tabla: Canal
------------------------------
- IdCanal (string)
- DescCanal (string)

Tabla: Cliente
------------------------------
- IdCategoria (string)
- Categoría (string)

Tabla: Compañia
------------------------------
- IdCompania (string)
- Compañía (string)

Tabla: Costo / Presupuesto
------------------------------
- IdPeriodo (string)
- IdCompania-IdProductoCompania (string)
- IdProductoCompania (string)
- IdCompania (string)
- IdCanal (string)
- IdProducto (int64)
- IdLinea (string)
- IdFamilia (string)
- IdAreaTerapeutica (string)
- IdIndicacion (string)
- IdPais (string)
- IdPais-IdZonaGestion (string)
- IdProductoMPh (int64)
- IdZonaGestion (string)
- IdTipoNegocio (string)
- IdTipoProducto (string)
- IdFabricante (int64)
- IdFormaFarmaceutica (string)
- ClasificacionOtcOtx (string)
- CostoConsolidado (double)
- CostoConsolidadoUnitario (double)
- FechaCostoConsolidado (int64)
- Fecha
- UNPresupuestada (double)
- UNEstimada (double)
- UNSTDPresupuestada (double)
- UNSTDEstimada (double)
- MLPresupuestado (double)
- MLEstimado (double)
- USDPresupuestado (double)
- USDEstimado (double)
- UNEstimadaMLB (double)
- UNSTDEstimadaMLB (double)
- MLEstimadoMLB (double)
- USDEstimadoMLB (double)
- QPresupuestado (double)
- QEstimado (double)
- TargetPRoduct (string)
- CovidProduct (string)
- MLPresupuestadoAjustado (double)
- Trim (string)
- UNEstimadaBC (double)
- UNSTDEstimadaBC (double)
- MLEstimadoBC (double)
- USDEstimadoBC (double)
- MarcaBud (string)

Tabla: DimMarcaBudg
------------------------------
- MarcaBud (string)
- ATBudg (string)

Tabla: EstimadoPptoBudget
------------------------------
- IdCompania-IdProductoCompania (string)
- MarcaBud (string)
- ATBudg (string)
- Categoria (string)
- CUnitEstimado (double)
- CUnitPresupuestado (double)
- Cantidad (int64)
- BusUnitBud (string)
- AnioEstimado (string)
- CostoEstimado (double)
- AnioPresupuesto (string)
- CostoPresupuesto (double)
- Origen (string)

Tabla: Fabricante
------------------------------
- IdFabricante (int64)
- Descripcion (string)

Tabla: Familia
------------------------------
- IdFamilia (string)
- Familia (string)
- Nombre Leading Products (string)

Tabla: Forma Farmacéutica
------------------------------
- IdFormaFarmaceutica (string)
- Forma Farmacéutica (string)
- IdTipoForma (string)
- CantStandard (int64)

Tabla: Key Product
------------------------------
- KeyProduct (string)

Tabla: Linea Comercial
------------------------------
- IdLinea (string)
- Línea Comercial (string)
- Laboratorio (string)

Tabla: Marca
------------------------------
- IdProducto (int64)
- Marca (string)
- KeyProduct (string)
- Leading Brands (string)
- IdMarca (string)
- Marca (grupos)

Tabla: País
------------------------------
- IdPais (string)
- DescPais (string)

Tabla: País / Zona-Gestión
------------------------------
- IdPais-IdZonaGestion (string)
- IdPais (string)
- DescripcionPais (string)
- IdZonaGestion (string)
- DescripcionZG (string)
- Zona Geográfica
- IdTipoNegocio (string)
- IdTipoCrecimiento (string)
- TipoZonaGestion (string)
- Zona Geográfica (groups)
- Img (string)
- Origen (string)
- DescripcionPaisIMS
- Zona Reporte Mensual
- DescripcionZG (Organic)
- DescripcionZG (Mega Own Lines)
- DescripcionZG (Exportaciones)
- DescripcionZG (Mega Pharma)
- DescripcionZG (Public Sales Ecuador)
- Región
- Grupo Gestiones (string)

Tabla: Período
------------------------------
- Anio (int64)
- Mes (int64)
- Fecha
- Quarter (string)

Tabla: Período a Analizar
------------------------------
- Año
- Mes
- Quarter
- Fecha

Tabla: Periodos MAT
------------------------------
- Periodo (string)
- Fecha (dateTime)
- Fecha ultima (dateTime)
- Index (int64)
- Real/Proy (string)
- Column6 (string)

Tabla: Producto MPh
------------------------------
- IdProductoMPh (int64)
- Producto MPh (string)
- IdProductoFabricante (string)

Tabla: Producto Compañía
------------------------------
- IdProductoCompania (string)
- Presentación (string)
- FechaLanzamiento (dateTime)
- IdCompania (string)
- IdCompania-IdProductoCompania (string)
- Fecha
- FechaLanzamientoQuarter

Tabla: SubFamilia
------------------------------
- IdProducto (int64)
- Marca (string)
- SubFamilia (string)

Tabla: Target Product
------------------------------
- Target Product (string)

Tabla: Tipo de Producto
------------------------------
- IdTipoProducto (string)
- Descripcion (string)

Tabla: Ventas Mensuales
------------------------------
- IdPeriodo (string)
- IdProductoCompania (string)
- IdCompania (string)
- IdCanal (string)
- IdProducto (int64)
- IdLinea (string)
- IdFamilia (string)
- IdAreaTerapeutica (string)
- IdIndicacion (string)
- IdPais (string)
- IdProductoMPh (int64)
- IdZonaGestion (string)
- UN (double)
- UNSTD (double)
- ML (double)
- USD (double)
- Fecha
- IdTipoNegocio (string)
- IdTipoProducto (string)
- IdFabricante (int64)
- IdFormaFarmaceutica (string)
- ClasificacionOtcOtx (string)
- IdCompania-IdProductoCompania (string)
- IdPais-IdZonaGestion (string)
- IdCliente (string)
- Q (double)
- TargetProduct (string)
- CovidProduct (string)
- CantidadElog (int64)
- CostoConsolidadoUnitario (double)
- UnidadOtros (double)
- IdProductoFabricante (string)
- PharmaceuticalDivision (string)
- Marca Paragua (string)
- CategoriaFamilia (string)
- Idzonageografica (string)

Tabla: Zona-Gestión
------------------------------
- IdZonaGestion (string)
- Descripcion (string)
- IdTipoNegocio (string)
- IdTipoCrecimiento (string)
- TipoZonaGestion (string)

