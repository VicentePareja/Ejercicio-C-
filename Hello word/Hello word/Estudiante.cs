using System;

namespace HelloWorld
{
    public class Estudiante
    {
        // Atributos de la clase
        private string nombre;
        private double[] notas;

        // Constructor de la clase
        public Estudiante(string name, int cantidad_notas)
        {
            this.nombre = name;
            this.notas = new double[cantidad_notas]; // Inicializa el arreglo de notas

            // Asigna a todas las notas el valor inicial de 1.0
            for (int i = 0; i < cantidad_notas; i++)
            {
                this.notas[i] = 1.0;
            }
        }

        // Métodos de la clase
        public void CambiarNota(int idNota, double nuevaNota)
        {
            // Comprueba que el índice de la nota esté en el rango correcto
            if (idNota >= 0 && idNota < notas.Length)
            {
                notas[idNota] = nuevaNota;
            }
        }

        public double ObtenerPromedio()
        {
            double suma = 0;
            foreach (double nota in notas)
            {
                suma += nota;
            }

            return suma / notas.Length;
        }

        public string ObtenerNombre()
        {
            return nombre;
        }
    }
}
