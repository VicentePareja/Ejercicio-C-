class Persona {
private string n ;
public Persona ( string n ) {
    this . n = n ;
    }
public void CambiarNombre ( string nombre ) {
    n = nombre ;
    }
public void MostrarNombre () {
    Console . WriteLine ( n ) ;
    }
}