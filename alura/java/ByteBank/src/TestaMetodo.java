
public class TestaMetodo {

	public static void main(String[] args) {
		Conta contaDaAmne = new Conta();
		Conta contaDoWagner = new Conta();
		contaDaAmne.deposita(500);
		System.out.println(contaDaAmne.saldo);
		contaDaAmne.saca(100);
		System.out.println(contaDaAmne.saldo);
		contaDaAmne.transfere(10, contaDoWagner);
		System.out.println(contaDaAmne.saldo);

		System.out.println("O saldo da conta da Amne �: R$ " + contaDaAmne.saldo);
		System.out.println("O saldo da conta do Wagner �: R$ " + contaDoWagner.saldo);
		
	}
	
}
