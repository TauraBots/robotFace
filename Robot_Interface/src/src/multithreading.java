package src;

import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JPanel;
import org.jfree.data.xy.XYSeries;

public class multithreading implements Runnable {

    protected JPanel jp;
    public Thread thread;
    protected XYSeries series;
    public boolean suspended = false;
    protected String motor;

    multithreading(JPanel jp, XYSeries series, String motor) {
        this.motor = motor;
        this.jp = jp;
        this.series = series;
        System.out.println("Creating " + motor);
    }

    @Override
    public void run() {
        System.out.println("Running " + motor);
        try {
            int contador = 0;
            double rad;
            while (true) {
                contador = contador + 2;
                rad = (Math.PI / 180) * contador;
                series.add(contador, Math.sin(rad));
                jp.repaint();
                Thread.sleep(40);
                synchronized (this) {
                    while (suspended) {
                        wait();
                    }
                }
            }
        } catch (InterruptedException ex) {
            Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
            System.out.println("Thread " + motor + " interrupted.");
        }
    }

    public void start() {
        System.out.println("Starting " + motor);
        if (thread == null) {
            thread = new Thread(this, motor);
            thread.start();
        }
    }

    void suspend() {
        suspended = true;
    }

    synchronized void resume() {
        suspended = false;
        notify();
    }
}
