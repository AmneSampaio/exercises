
public class Gerente extends Funcionario implements Autenticavel{	
	
	private MetodoLogin login;

	public Gerente() {
		this.login = new MetodoLogin();
	}
	public void setSenha(int senha) {
		this.login.setSenha(senha);
		
	}

	public boolean autentica(int senha) {
		return this.login.autentica(senha);
	}	
	public double  getBonificacao() {
		return super.getSalario();
	}
}