
public class TesteFuncionario {

	public static void main(String[] args) {

		Funcionario amne = new Gerente();
		amne.setNome("Amne Fredo");
		amne.setCpf("000.000.000-00");
		amne.setSalario(3500.0);
		
		System.out.println(amne.getNome());
		System.out.println(amne.getBonificacao());
		
	}

}
