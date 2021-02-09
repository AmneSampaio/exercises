
public class Cliente implements Autenticavel {

	private MetodoLogin login;
	
	public Cliente() {
		this.login = new MetodoLogin();
	}
	public void setSenha(int senha) {
		this.login.setSenha(senha);
		
	}

	public boolean autentica(int senha) {
		return this.login.autentica(senha);
	
	
	}
}