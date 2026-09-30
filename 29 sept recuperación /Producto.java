package producto;


public class Product {
    private String nombre;
    private String categorias;
    private double precio;
    private int cantidadStock;
    
    public Product(){  
    }
    
    public Product(String nombre , String categorias , double precio , int cantidadStock){
        this.nombre=nombre;
        this.categorias=categorias;
        this.precio=precio;
        this.cantidadStock=cantidadStock;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getCategorias() {
        return categorias;
    }

    public void setCategorias(String categorias) {
        this.categorias = categorias;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    public int getCantidadStock() {
        return cantidadStock;
    }

    public void setCantidadStock(int cantidadStock) {
        this.cantidadStock = cantidadStock;
    }
    
    
    public String verDetalle(){
        String estadistica="nombre:"+this.nombre+"\n"
        +"categorias:"+this.categorias+"\n"
        +"precio:"+this.precio+"\n"
        +"cantidad:"+this.cantidadStock;
        
        return estadistica;  
    }
    
    public double calcularDescuento(int porcentaje){
        double descuento=(this.precio * porcentaje / 1000);
        
        return descuento;
    }
    
    public double calcularDescuento(double porcentaje){
        double descuento1=(this.precio * porcentaje /1000);
        
        return descuento1;
    }
    
    public double calcularPrecioFinal(double porcentaje){
        double descuentoTotal=this.calcularDescuento(porcentaje);
        
        double precioFinal=(precio - descuentoTotal);
        
        return precioFinal;
    }
    
    
    public String vender(int cantidad){
        if (cantidad <= this.cantidadStock){
            this.cantidadStock=this.cantidadStock-1;
            return "venta realizada quedan "+this.cantidadStock+" unidades";
        }else{
            return "no hay suficientes inventario";
        }
    }
    
   
}




public class Producto {

   
    public static void main(String[] args) {
        Product lampara=new Product("lampara","funcional",1000,3);
        
        String estadisticas =lampara.verDetalle();
        double descuentoFinal=lampara.calcularDescuento(2);
        double descuentoFinal2=lampara.calcularDescuento(2.5);
        double precioTotal=lampara.calcularPrecioFinal(2.5);
  
        String VenderProducto=lampara.vender(1);
        
        
        
     
    }
    
}
