
public class TesteReferencias {

	public static void main(String[] args) {
		Conta primeiraConta = new Conta();
		primeiraConta.saldo = 300;
		
		System.out.println("Saldo da primeira conta: " + primeiraConta.saldo);
		
		Conta segundaConta = primeiraConta;
		System.out.println("Saldo da segunda conta: " + segundaConta.saldo);
		
		segundaConta.saldo = 200;
		segundaConta.deposita(1000);
		System.out.println("Saldo da segunda conta: " + segundaConta.saldo);
		System.out.println("Saldo da primeira conta: " + primeiraConta.saldo);
		
		if (primeiraConta == segundaConta){
			System.out.println("S�o iguais");
			System.out.println(primeiraConta);
		} else {
			System.out.println("S�o diferentes");
			System.out.println("Primeira conta: " + primeiraConta + " " + "Segunda conta: " + segundaConta);
		}
	}
}