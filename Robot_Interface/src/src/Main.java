package src;

import java.awt.BorderLayout;
import java.awt.Color;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

public class Main extends javax.swing.JFrame {

    XYSeries series1 = new XYSeries("Motor Servo Angles");
    XYSeries series2 = new XYSeries("Motor Servo Angles");
    XYSeries series3 = new XYSeries("Motor Servo Angles");
    XYSeries series4 = new XYSeries("Motor Servo Angles");
    XYSeries series5 = new XYSeries("Motor Servo Angles");
    XYSeries series6 = new XYSeries("Motor Servo Angles");
    XYSeries series7 = new XYSeries("Motor Servo Angles");
    XYSeries series8 = new XYSeries("Motor Servo Angles");
    XYSeries series9 = new XYSeries("Motor Servo Angles");
    XYSeries series10 = new XYSeries("Motor Servo Angles");
    XYSeries series11 = new XYSeries("Motor Servo Angles");
    XYSeries series12 = new XYSeries("Motor Servo Angles");
    

    multithreading m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12;
    int running = 0;

    
    public Main() {
        initComponents();
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        jPanel2 = new javax.swing.JPanel();
        jPanel3 = new javax.swing.JPanel();
        jPanel4 = new javax.swing.JPanel();
        jButton1 = new javax.swing.JButton();
        jPanel5 = new javax.swing.JPanel();
        jPanel6 = new javax.swing.JPanel();
        jPanel7 = new javax.swing.JPanel();
        jPanel8 = new javax.swing.JPanel();
        jButton2 = new javax.swing.JButton();
        jPanel9 = new javax.swing.JPanel();
        jPanel10 = new javax.swing.JPanel();
        jPanel11 = new javax.swing.JPanel();
        jPanel12 = new javax.swing.JPanel();
        jSeparator1 = new javax.swing.JSeparator();
        jLabel1 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        jLabel6 = new javax.swing.JLabel();
        jLabel7 = new javax.swing.JLabel();
        jLabel8 = new javax.swing.JLabel();
        jLabel9 = new javax.swing.JLabel();
        jLabel10 = new javax.swing.JLabel();
        jLabel11 = new javax.swing.JLabel();
        jLabel12 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Motor Angles");
        setBackground(new java.awt.Color(254, 254, 254));
        addWindowListener(new java.awt.event.WindowAdapter() {
            public void windowOpened(java.awt.event.WindowEvent evt) {
                formWindowOpened(evt);
            }
        });
        getContentPane().setLayout(null);

        jPanel1.setLayout(new java.awt.BorderLayout());
        getContentPane().add(jPanel1);
        jPanel1.setBounds(260, 20, 230, 140);

        jPanel2.setLayout(new java.awt.BorderLayout());
        getContentPane().add(jPanel2);
        jPanel2.setBounds(500, 20, 230, 140);

        jPanel3.setLayout(new java.awt.BorderLayout());
        getContentPane().add(jPanel3);
        jPanel3.setBounds(260, 170, 230, 140);

        jPanel4.setLayout(new java.awt.BorderLayout());
        getContentPane().add(jPanel4);
        jPanel4.setBounds(500, 170, 230, 140);

        jButton1.setText("Iniciar gráficos");
        jButton1.setFocusable(false);
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });
        getContentPane().add(jButton1);
        jButton1.setBounds(60, 50, 130, 40);

        jPanel5.setLayout(new java.awt.BorderLayout());
        getContentPane().add(jPanel5);
        jPanel5.setBounds(260, 320, 230, 140);

        jPanel6.setLayout(new java.awt.BorderLayout());
        getContentPane().add(jPanel6);
        jPanel6.setBounds(500, 320, 230, 140);

        jPanel7.setLayout(new java.awt.BorderLayout());
        getContentPane().add(jPanel7);
        jPanel7.setBounds(740, 20, 230, 140);

        jPanel8.setLayout(new java.awt.BorderLayout());
        getContentPane().add(jPanel8);
        jPanel8.setBounds(980, 20, 230, 140);

        jButton2.setText("Parar gráficos");
        jButton2.setFocusable(false);
        jButton2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton2ActionPerformed(evt);
            }
        });
        getContentPane().add(jButton2);
        jButton2.setBounds(60, 100, 130, 40);

        jPanel9.setLayout(new java.awt.BorderLayout());
        getContentPane().add(jPanel9);
        jPanel9.setBounds(980, 170, 230, 140);

        jPanel10.setLayout(new java.awt.BorderLayout());
        getContentPane().add(jPanel10);
        jPanel10.setBounds(740, 170, 230, 140);

        jPanel11.setLayout(new java.awt.BorderLayout());
        getContentPane().add(jPanel11);
        jPanel11.setBounds(980, 320, 230, 140);

        jPanel12.setLayout(new java.awt.BorderLayout());
        getContentPane().add(jPanel12);
        jPanel12.setBounds(740, 320, 230, 140);
        getContentPane().add(jSeparator1);
        jSeparator1.setBounds(40, 180, 170, 10);

        jLabel1.setText("Motor 1: ");
        getContentPane().add(jLabel1);
        jLabel1.setBounds(30, 220, 110, 30);

        jLabel2.setText("Motor 2: ");
        getContentPane().add(jLabel2);
        jLabel2.setBounds(30, 260, 110, 30);

        jLabel3.setText("Motor 3: ");
        getContentPane().add(jLabel3);
        jLabel3.setBounds(30, 300, 110, 30);

        jLabel4.setText("Motor 4: ");
        getContentPane().add(jLabel4);
        jLabel4.setBounds(30, 340, 110, 30);

        jLabel5.setText("Motor 5: ");
        getContentPane().add(jLabel5);
        jLabel5.setBounds(30, 380, 110, 30);

        jLabel6.setText("Motor 6: ");
        getContentPane().add(jLabel6);
        jLabel6.setBounds(30, 420, 110, 30);

        jLabel7.setText("Motor 7: ");
        getContentPane().add(jLabel7);
        jLabel7.setBounds(140, 220, 110, 30);

        jLabel8.setText("Motor 8: ");
        getContentPane().add(jLabel8);
        jLabel8.setBounds(140, 260, 110, 30);

        jLabel9.setText("Motor 9: ");
        getContentPane().add(jLabel9);
        jLabel9.setBounds(140, 300, 110, 30);

        jLabel10.setText("Motor 10: ");
        getContentPane().add(jLabel10);
        jLabel10.setBounds(140, 340, 110, 30);

        jLabel11.setText("Motor 11: ");
        getContentPane().add(jLabel11);
        jLabel11.setBounds(140, 380, 110, 30);

        jLabel12.setText("Motor 12: ");
        getContentPane().add(jLabel12);
        jLabel12.setBounds(140, 420, 110, 30);

        setSize(new java.awt.Dimension(1239, 529));
        setLocationRelativeTo(null);
    }// </editor-fold>//GEN-END:initComponents

    private void formWindowOpened(java.awt.event.WindowEvent evt) {//GEN-FIRST:event_formWindowOpened
        getContentPane().setBackground(Color.white);
        jButton2.setEnabled(false);
        
        XYSeriesCollection dataset1 = new XYSeriesCollection(series1);
        series1.setMaximumItemCount(200);
        XYSeriesCollection dataset2 = new XYSeriesCollection(series2);
        series2.setMaximumItemCount(200);
        XYSeriesCollection dataset3 = new XYSeriesCollection(series3);
        series3.setMaximumItemCount(200);
        XYSeriesCollection dataset4 = new XYSeriesCollection(series4);
        series4.setMaximumItemCount(200);
        XYSeriesCollection dataset5 = new XYSeriesCollection(series5);
        series5.setMaximumItemCount(200);
        XYSeriesCollection dataset6 = new XYSeriesCollection(series6);
        series6.setMaximumItemCount(200);
        XYSeriesCollection dataset7 = new XYSeriesCollection(series7);
        series7.setMaximumItemCount(200);
        XYSeriesCollection dataset8 = new XYSeriesCollection(series8);
        series8.setMaximumItemCount(200);
        XYSeriesCollection dataset9 = new XYSeriesCollection(series9);
        series9.setMaximumItemCount(200);
        XYSeriesCollection dataset10 = new XYSeriesCollection(series10);
        series10.setMaximumItemCount(200);
        XYSeriesCollection dataset11 = new XYSeriesCollection(series11);
        series11.setMaximumItemCount(200);
        XYSeriesCollection dataset12 = new XYSeriesCollection(series12);
        series12.setMaximumItemCount(200);
        
        JFreeChart chart1 = ChartFactory.createXYLineChart("Motor 1", "", "", dataset1, PlotOrientation.VERTICAL, false, true, true);
        JFreeChart chart2 = ChartFactory.createXYLineChart("Motor 2", "", "", dataset2, PlotOrientation.VERTICAL, false, true, true);
        JFreeChart chart3 = ChartFactory.createXYLineChart("Motor 3", "", "", dataset3, PlotOrientation.VERTICAL, false, true, true);
        JFreeChart chart4 = ChartFactory.createXYLineChart("Motor 4", "", "", dataset4, PlotOrientation.VERTICAL, false, true, true);
        JFreeChart chart5 = ChartFactory.createXYLineChart("Motor 5", "", "", dataset1, PlotOrientation.VERTICAL, false, true, true);
        JFreeChart chart6 = ChartFactory.createXYLineChart("Motor 6", "", "", dataset2, PlotOrientation.VERTICAL, false, true, true);
        JFreeChart chart7 = ChartFactory.createXYLineChart("Motor 7", "", "", dataset3, PlotOrientation.VERTICAL, false, true, true);
        JFreeChart chart8 = ChartFactory.createXYLineChart("Motor 8", "", "", dataset4, PlotOrientation.VERTICAL, false, true, true);
        JFreeChart chart9 = ChartFactory.createXYLineChart("Motor 9", "", "", dataset1, PlotOrientation.VERTICAL, false, true, true);
        JFreeChart chart10 = ChartFactory.createXYLineChart("Motor 10", "", "", dataset2, PlotOrientation.VERTICAL, false, true, true);
        JFreeChart chart11 = ChartFactory.createXYLineChart("Motor 11", "", "", dataset3, PlotOrientation.VERTICAL, false, true, true);
        JFreeChart chart12 = ChartFactory.createXYLineChart("Motor 12", "", "", dataset4, PlotOrientation.VERTICAL, false, true, true);

        jPanel1.add(new ChartPanel(chart1), BorderLayout.CENTER);
        jPanel1.setMinimumSize(jPanel1.getMaximumSize());
        jPanel2.add(new ChartPanel(chart2), BorderLayout.CENTER);
        jPanel2.setMinimumSize(jPanel2.getMaximumSize());
        jPanel3.add(new ChartPanel(chart3), BorderLayout.CENTER);
        jPanel3.setMinimumSize(jPanel3.getMaximumSize());
        jPanel4.add(new ChartPanel(chart4), BorderLayout.CENTER);
        jPanel4.setMinimumSize(jPanel4.getMaximumSize());
        jPanel5.add(new ChartPanel(chart5), BorderLayout.CENTER);
        jPanel5.setMinimumSize(jPanel5.getMaximumSize());
        jPanel6.add(new ChartPanel(chart6), BorderLayout.CENTER);
        jPanel6.setMinimumSize(jPanel6.getMaximumSize());
        jPanel7.add(new ChartPanel(chart7), BorderLayout.CENTER);
        jPanel7.setMinimumSize(jPanel7.getMaximumSize());
        jPanel8.add(new ChartPanel(chart8), BorderLayout.CENTER);
        jPanel8.setMinimumSize(jPanel8.getMaximumSize());
        jPanel9.add(new ChartPanel(chart9), BorderLayout.CENTER);
        jPanel9.setMinimumSize(jPanel9.getMaximumSize());
        jPanel10.add(new ChartPanel(chart10), BorderLayout.CENTER);
        jPanel10.setMinimumSize(jPanel10.getMaximumSize());
        jPanel11.add(new ChartPanel(chart11), BorderLayout.CENTER);
        jPanel11.setMinimumSize(jPanel11.getMaximumSize());
        jPanel12.add(new ChartPanel(chart12), BorderLayout.CENTER);
        jPanel12.setMinimumSize(jPanel12.getMaximumSize());

        createThreads();

    }//GEN-LAST:event_formWindowOpened

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
        jButton1.setEnabled(false);
        jButton2.setEnabled(true);

        if (running == 0) {
            running = 1;
            m1.start();
            m2.start();
            m3.start();
            m4.start();
            m5.start();
            m6.start();
            m7.start();
            m8.start();
            m9.start();
            m10.start();
            m11.start();
            m12.start();
        } else {
            m1.resume();
            m2.resume();
            m3.resume();
            m4.resume();
            m5.resume();
            m6.resume();
            m7.resume();
            m8.resume();
            m9.resume();
            m10.resume();
            m11.resume();
            m12.resume();
        }
    }//GEN-LAST:event_jButton1ActionPerformed

    private void jButton2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton2ActionPerformed
        jButton1.setEnabled(true);
        jButton2.setEnabled(false);

        m1.suspend();
        m2.suspend();
        m3.suspend();
        m4.suspend();
        m5.suspend();
        m6.suspend();
        m7.suspend();
        m8.suspend();
        m9.suspend();
        m10.suspend();
        m11.suspend();
        m12.suspend();
        
    }//GEN-LAST:event_jButton2ActionPerformed

    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException | InstantiationException | IllegalAccessException | javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Main.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(() -> {
            new Main().setVisible(true);
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton jButton1;
    private javax.swing.JButton jButton2;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel10;
    private javax.swing.JLabel jLabel11;
    private javax.swing.JLabel jLabel12;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JLabel jLabel9;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPanel10;
    private javax.swing.JPanel jPanel11;
    private javax.swing.JPanel jPanel12;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JPanel jPanel3;
    private javax.swing.JPanel jPanel4;
    private javax.swing.JPanel jPanel5;
    private javax.swing.JPanel jPanel6;
    private javax.swing.JPanel jPanel7;
    private javax.swing.JPanel jPanel8;
    private javax.swing.JPanel jPanel9;
    private javax.swing.JSeparator jSeparator1;
    // End of variables declaration//GEN-END:variables

    public void createThreads() {
        m1 = new multithreading(jPanel1, series1, "Motor1");
        m2 = new multithreading(jPanel2, series2, "Motor2");
        m3 = new multithreading(jPanel3, series3, "Motor3");
        m4 = new multithreading(jPanel4, series4, "Motor4");
        m5 = new multithreading(jPanel5, series5, "Motor5");
        m6 = new multithreading(jPanel6, series6, "Motor6");
        m7 = new multithreading(jPanel7, series7, "Motor7");
        m8 = new multithreading(jPanel8, series8, "Motor8");
        m9 = new multithreading(jPanel9, series9, "Motor9");
        m10 = new multithreading(jPanel10, series10, "Motor10");
        m11 = new multithreading(jPanel11, series11, "Motor11");
        m12 = new multithreading(jPanel12, series12, "Motor12");
    }
}
