import java.rmi.Remote;
import java.rmi.RemoteException;

public interface PrintMessage extends Remote {

    void printMessage() throws RemoteException;

}
