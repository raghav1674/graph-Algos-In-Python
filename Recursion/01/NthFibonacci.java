import java.util.HashMap;

class NthFibonacci{


	public static int nthFibonacci(int n){

		if(n==1 || n==2)return n-1;

		return nthFibonacci(n-1) + nthFibonacci(n-2);
	}

	private static HashMap<Integer,Integer>dp = new HashMap<>();
	public static int memFibonacci(int n){

		if(n==1 || n==2)return n-1;

		if(!dp.containsKey(n))

			dp.put(n,memFibonacci(n-1) + memFibonacci(n-2));
		return dp.get(n);

		
	}

	public static int topDownFibonacci(int n){


		if(n==1 || n==2)return n-1;

		int a =0,b=1;
		for(int i=2;i<n;i++){

			a = b;
			b = a+b;
		}
		return b;
	}


	public static void main(String[] args) {
		System.out.println(memFibonacci(8));
	}

}