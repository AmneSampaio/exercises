public class impostoDeRenda {

    public static void main(String[] args) {

        double salario = 4000.0;

        // De 1900.0 at� 2800.0, o IR � de 7.5% e pode deduzir na declara��o o valor de R$ 142
        // De 2800.01 at� 3751.0, o IR � de 15% e pode deduzir R$ 350
        // De 3751.01 at� 4664.00, o IR � de 22.5% e pode deduzir R$ 636
        
        if (salario >= 1900 && salario <= 2800) {
        	// double coletadoIr = salario*0.075;
        	System.out.println("Seu sal�rio � R$ " + salario + " e se encaixa no grupo 1 (al�quota de 7.5 %). "
        			+ "O valor deduzido pode ser de at� R$ 142");
        } else if (salario >= 2800.01 && salario <= 3751) {
        	// double coletadoIr = salario*0.15;
        	System.out.println("Seu sal�rio � R$ " + salario + " e se encaixa no grupo 2 (al�quota de 15 %). "
        			+ "O valor deduzido pode ser de at� R$ 350");
        } else if (salario >= 3751 && salario <= 4664.00) {
        	// double coletadoIr = salario*0.225;
        	System.out.println("Seu sal�rio � R$ " + salario + " e se encaixa no grupo 3 (al�quota de 22.5 %). "
        			+ "O valor deduzido pode ser de at� R$ 636");
        }
    }
}

