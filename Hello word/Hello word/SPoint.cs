namespace HelloWorld;

struct SPoint {
private int _x ;
private int _y ;
public SPoint ( int x , int y ) {
    _x = x ;
    _y = y ;
    }
public void Square () {
    _x = _x * _x ;
    _y = _y * _y ;
    }
public void Print () { Console . WriteLine ( $" ({ _x } ,{ _y }) " ) ; }
}