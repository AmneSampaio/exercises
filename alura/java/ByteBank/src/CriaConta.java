
public class CriaConta {
	public static void main(String[] args) {
		Conta primeiraConta = new Conta();
		primeiraConta.saldo = 200;
		System.out.println("Conta criada! ");
		System.out.println("O saldo � de R$ " + primeiraConta.saldo );
		
		Conta segundaConta = new Conta();
		
		if (primeiraConta == segundaConta){
			System.out.println("S�o iguais");
			System.out.println(primeiraConta);
		} else {
			System.out.println("S�o diferentes");
			System.out.println("Primeira conta: " + primeiraConta + " " + "Segunda conta: " + segundaConta);
		}
 	}
}