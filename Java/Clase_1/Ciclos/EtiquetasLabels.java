
package Ciclos;

public class EtiquetasLabels {
    public static void main(String[] args) {
      
 //Uso de las palabras break  junto a la etiqueta(labels)
        inicio: //Etiquetas (Labels) Se combinan con break o continue.NO es recomendable        
        for (var contando = 0; contando < 7 ; contando++ ){
             if(contando % 2 == 0){
                 System.out.println("contando = " + contando);
                 break inicio;//Sin el break.Mostrara todas las posiciones de pares
            }
        }
    }
    
}
