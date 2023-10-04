abstract class Test1{ 
	abstract void mt(); 
} 

class Test2 extends Test1{ 
	void mt() { 
		System.out.println("Inside Test2 mt method"); 
	} 
} 

class Test3 extends Test1{ 
	void mt() { 
		System.out.println("Inside Test3 mt method"); 
	} 
} 

public class stringBuffer { 
	public static void main(String[] args) { 
		Test1 ref; 

		ref=new Test2(); 
		ref.mt(); 

		ref=new Test3(); 
		ref.mt(); 
	} 
} 