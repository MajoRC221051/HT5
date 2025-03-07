import random
import numpy as np
import matplotlib.pyplot as plt

# Función que simula el tiempo de ejecución de los procesos con intervalos de llegada
def simulate_processes(num_processes, interval):
    # Los tiempos de los procesos se generan aleatoriamente entre 1 y 10 segundos
    process_times = [random.uniform(1, 10) for _ in range(num_processes)]
    # Los procesos llegan en intervalos especificados (5 segundos o 1 segundo)
    arrival_times = [i * interval for i in range(num_processes)]
    return arrival_times, process_times

# Función para calcular el promedio y la desviación estándar
def calculate_stats(process_times):
    avg_time = np.mean(process_times)
    std_dev = np.std(process_times)
    return avg_time, std_dev

# Lista de número de procesos para simular
num_processes_list = [25, 50, 100, 150, 200]
intervals = [10, 5, 1]  # Intervalos de llegada de los procesos: 5 segundos y 1 segundo

# Almacenar los resultados
avg_times = {interval: [] for interval in intervals}
std_devs = {interval: [] for interval in intervals}

# Simular los procesos y calcular las estadísticas para cada cantidad de procesos
for interval in intervals:
    for num_processes in num_processes_list:
        print(f"Simulación con {num_processes} procesos y un intervalo de {interval} segundos:")
        arrival_times, process_times = simulate_processes(num_processes, interval)
        
        # Mostrar los tiempos de los procesos individuales
        print(f"Tiempos de ejecución de los procesos: {process_times}")
        
        # Calcular el promedio y la desviación estándar de los tiempos de ejecución
        avg_time, std_dev = calculate_stats(process_times)
        avg_times[interval].append(avg_time)
        std_devs[interval].append(std_dev)
        
        # Mostrar las estadísticas
        print(f"Tiempo promedio: {avg_time:.2f} segundos")
        print(f"Desviación estándar: {std_dev:.2f} segundos")
        print("-" * 50)

# Graficar los resultados
plt.figure(figsize=(10,6))
for interval in intervals:
    plt.plot(num_processes_list, avg_times[interval], label=f"Intervalo {interval}s (Promedio)", marker='o')
    plt.plot(num_processes_list, std_devs[interval], label=f"Intervalo {interval}s (Desviación Estándar)", marker='x')

plt.xlabel('Número de Procesos')
plt.ylabel('Tiempo (segundos)')
plt.title('Simulación de Tiempo Promedio y Desviación Estándar con Diferentes Intervalos')
plt.legend()
plt.grid(True)
plt.show()

