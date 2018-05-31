import java.rmi.RemoteException;

public class Greet implements PrintMessage {
    @Override
    public void printMessage(){

        System.out.println("Welcome to Remote Procedure");

    }
}
