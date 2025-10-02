package exercicio1;

public class Main {

	public static void main(String[] args) {
		Avaliacao luigi = new Avaliacao(8,9,5);
		Avaliacao mario = new Avaliacao(7,4,10);
		
		System.out.println("Media Aritmetica do Mario: " + mario.mediaAritmetica());
		System.out.println("Media Aritmetica do Mario: " + mario.mediaPonderada());
		
		System.out.println("Media Aritmetica do Luigi: " + luigi.mediaAritmetica());
		System.out.println("Media Aritmetica do Luigi: " + luigi.mediaPonderada());
	}

}
