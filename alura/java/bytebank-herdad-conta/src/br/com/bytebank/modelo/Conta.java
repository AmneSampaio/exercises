package br.com.bytebank.modelo;

public abstract class Conta{
	protected double saldo;
	private int agencia;
	private int numero;
	private Cliente titular;
	private static int total = 0;
	
	
	public Conta(int agencia, int numero) {
		total++;
		//System.out.println("O total de contas � " + Conta.total);
		this.agencia = agencia;
		this.numero = numero;
		//System.out.println("A agencia � " + this.agencia + " e a conta � " + this.numero
		//		+ ". ");
	}
	
	public static int getTotal() {
		return Conta.total;
	}
	
	
	
	public abstract void deposita(double valor); 
	//	this.saldo += valor;
		
	
	
	public void saca(double valor) throws SaldoInsuficienteException {
		
		
		if(this.saldo < valor) {
			throw new SaldoInsuficienteException("Saldo: " + this.saldo + ", Valor a sacar: " + valor);
		}
		
		this.saldo -= valor;
		
	}
	
	public void transfere(double valor, Conta destino) throws SaldoInsuficienteException{
		this.saca(valor);
		destino.deposita(valor);
	}
	
	public double getSaldo() {
		return this.saldo;
	}
	
	public int getNumero() {
		return this.numero;
	}
	
	public int getAgencia() {
		return this.agencia;
	}
	
	public void setAgencia(int agencia) {
		this.agencia = agencia;
	}
	
	public void setNumero(int numero) {
		this.numero = numero;
	}
	
	public Cliente getTitular() {
		return titular;
	}

	public void setTitular(Cliente titular) {
		this.titular = titular;
	}



}

