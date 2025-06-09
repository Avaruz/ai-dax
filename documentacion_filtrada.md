# Documentación del Modelo de Datos

*Documentación filtrada - Tablas incluidas: Ventas Mensuales, Producto Compañía, Área Terapéutica*

------------------------------
Tabla: Área Terapéutica
------------------------------
- IdAreaTerapeutica (string)
- Área Terapéutica (string)
- ImgAreaTerapeutica (string)
- Nombre Leading (string)
- Área Terapéutica BI
- Área Terapéutica BI (KeyProduct)
- Área Terapéutica BI (English)

------------------------------
Tabla: Producto Compañía
------------------------------
- IdProductoCompania (string)
- Presentación (string)
- FechaLanzamiento (dateTime)
- IdCompania (string)
- IdCompania-IdProductoCompania (string)
- Fecha
- FechaLanzamientoQuarter

------------------------------
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

