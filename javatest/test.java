class test {
    public static void main(String[] args){
        int x = 1;
        int inner(){
            x += 1;
        }
        inner();
        System.out.println("hello world");
        System.out.println(x);
    }
}
