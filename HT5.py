import random
import numpy as np
import matplotlib.pyplot as plt

# Función que simula el tiempo de ejecución de los procesos
def simulate_processes(num_processes, memory, seed):
    random.seed(seed)  # Establecer la semilla para generar resultados reproducibles
    # Generar tiempos de ejecución entre 1000 y 5000 segundos para hacerlo más realista
    process_times = [random.uniform(1000, 5000) for _ in range(num_processes)]
    return process_times

# Función para calcular el promedio y la desviación estándar
def calculate_stats(process_times):
    avg_time = np.mean(process_times)
    std_dev = np.std(process_times)
    return avg_time, std_dev

# Lista de número de procesos para simular (ahora incluyendo 25 como mencionaste)
num_processes_list = [25, 50, 100, 150, 200]

# Almacenar los resultados
avg_times = []
std_devs = []

# Establecer una semilla aleatoria fija para reproducibilidad
seed = 42  # Puedes cambiar la semilla si lo deseas

# i. Simulación con memoria 100 y sin otros cambios (solo un procesador)
print("Simulando con memoria normal (100)...")
for num_processes in num_processes_list:
    print(f"\nProcesos simulados con {num_processes} procesos:")

    process_times = simulate_processes(num_processes, memory=100, seed=seed)
    avg_time, std_dev = calculate_stats(process_times)
    avg_times.append(avg_time)
    std_devs.append(std_dev)

    # Mostrar las estadísticas
    print(f"Tiempos de ejecución de los procesos: {process_times}")
    print(f"Tiempo promedio: {avg_time:.2f} segundos")
    print(f"Desviación estándar: {std_dev:.2f} segundos")
    print("-" * 50)

# Graficar los resultados
plt.figure(figsize=(10,6))
plt.plot(num_processes_list, avg_times, label="Tiempo Promedio", marker='o', color='b')
plt.plot(num_processes_list, std_devs, label="Desviación Estándar", marker='o', color='r')
plt.xlabel('Número de Procesos')
plt.ylabel('Tiempo (segundos)')
plt.title('Simulación de Tiempo Promedio y Desviación Estándar con Memoria 100')
plt.legend()
plt.grid(True)
plt.show()
