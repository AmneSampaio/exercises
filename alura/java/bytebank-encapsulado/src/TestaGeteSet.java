
public class TestaGeteSet {
	public static void main(String[] args) {
		Cliente cliente = new Cliente();
		Conta conta = new Conta(1223,45567);
		cliente.setNome("Amne Fredo");
		conta.setTitular(cliente);
		
		System.out.println(conta.getTitular().getNome());
		conta.getTitular().setProfissao("progrmadora");
		System.out.println(conta.getTitular().getProfissao());
		System.out.println(Conta.getTotal());

		
		
	}
}
