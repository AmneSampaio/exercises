
public class CriaConta {
	public static void main(String[] args) {
		Conta primeiraConta = new Conta();
		primeiraConta.saldo = 200;
		System.out.println("Conta criada! ");
		System.out.println("O saldo é de R$ " + primeiraConta.saldo );
		
		Conta segundaConta = new Conta();
		
		if (primeiraConta == segundaConta){
			System.out.println("São iguais");
			System.out.println(primeiraConta);
		} else {
			System.out.println("São diferentes");
			System.out.println("Primeira conta: " + primeiraConta + " " + "Segunda conta: " + segundaConta);
		}
 	}
}