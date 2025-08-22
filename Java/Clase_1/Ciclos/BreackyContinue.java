
package Ciclos;

public class BreackyContinue {
    public static void main(String[] args) {
         //Etiquetas (Labels) Se combinan con break o continue.NO es recomendable  
        inicio:        
        for (var contando = 0; contando < 7 ; contando++ ){
             if(contando % 2 == 0){
                 System.out.println("contando = " + contando);
                 break inicio;//Sin el break.Mostrara todas las posiciones de pares
               }
          }
     }            
}
