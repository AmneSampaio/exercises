
public class TestaBanco {

	public static void main(String[] args) {
		Conta contaDaAmne = new Conta();
		//Cliente amne = new Cliente();
		contaDaAmne.titular = new Cliente();
		contaDaAmne.titular.nome = "Amne Sampaio Fredo";
		contaDaAmne.titular.cpf = "000.000.000-00";
		contaDaAmne.titular.profissao = "programadora";
		
		contaDaAmne.deposita(3000);
		//contaDaAmne.titular = amne; 
		String nome = contaDaAmne.titular.nome;		
		String profissao = contaDaAmne.titular.profissao;
		System.out.println(" O titular dessa conta se chama " + nome + " e sua profissão é " + profissao + ".");
		
	}

}
