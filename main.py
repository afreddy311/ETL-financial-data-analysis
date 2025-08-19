from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def run_pipeline():
    # Definir rutas de entrada y salida
    input_path = 'data/transacciones_financieras.csv'
    output_path = 'data/resumen_gastos_mensual.csv'

    # 1. Extraer
    df_raw = extract_data(input_path)

    # 2. Transformar
    df_transformed = transform_data(df_raw)

    # 3. Cargar
    load_data(df_transformed, output_path)

if __name__ == "__main__":
    run_pipeline()