//Clase 1(13/8)-Ciclos
package CicloWhile;

public class EjercicioWhile01 {
    public static void main(String[] args) {
         //Cilo While sintaxis
        System.out.println("Inicio de la sintaxisciclo While");
        var conteo = 0;//Inferencia de tipos
        while(conteo < 3 ){
            System.out.println("conteo = " + conteo);
            conteo++; //Vamos aumentando en uno la variable
        }
        
        //Ciclo do While sintaxis
        System.out.println("Inicio de la sintaxis del ciclo  do While");
        var contador = 0;
        do{
             System.out.println("contador = " + contador);
             contador++;
        }while(contador <= 7);//Nos mostrara 8 posiciones
        
 //Ciclo for sintaxis.(variable;Condicion;Incremento o decremento)
 //Uso de las palabras break y continue junto a las etiquetas(labels
         System.out.println("Inicio de la sintaxis del ciclo for,palabra break, continue y labels");
        inicio: //Etiquetas (Labels) Se combinan con break o continue.NO es recomendable        
        for (var contando = 0; contando < 7 ; contando++ ){
             if(contando % 2 == 0){
                 System.out.println("contando = " + contando);
                 break inicio;//Sin el break.Mostrara todas las posiciones de pares
            }
        }
         System.out.println("Inicio de la sintaxis del ciclo for y palabra continue");
        for (var contando = 0; contando < 7 ; contando++ ){
             if(contando % 2 != 0){
                 continue;//Vamos a la siguiente iteracion//Mostrara todos los pares
            }
              System.out.println("contando = " + contando);
             
        }
     }
}
