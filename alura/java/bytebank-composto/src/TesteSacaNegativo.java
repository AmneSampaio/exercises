
public class TesteSacaNegativo {

	public static void main(String[] args) {
		Conta conta = new Conta();
		conta.deposita(100);
				
		if (conta.saca(200) == true) {
		System.out.println("Saque realizado! Seu novo saldo é: " + conta.getSaldo());
		} else {
		System.out.println("Saque negado, por favor realize "
				+ "um depósito e tente novamente: R$ " + conta.getSaldo());
	
		}
	}
}
