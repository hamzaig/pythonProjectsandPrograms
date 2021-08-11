class A{
    void show(){
        cout<<"hello A"
    }
}

class B extends A{
    void show(){
        cout<<"hello B"
    }
}

main{
    A hamza = new B();
    hamza.show();
}