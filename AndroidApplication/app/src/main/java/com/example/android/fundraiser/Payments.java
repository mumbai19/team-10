package com.example.android.fundraiser;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.razorpay.Checkout;
import com.razorpay.PaymentResultListener;

import org.json.JSONObject;

public class Payments extends AppCompatActivity implements PaymentResultListener {

    int final_amount;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_payments);
        Button pay = (Button)findViewById(R.id.Pay);
        pay.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                EditText edtEditText = (EditText)findViewById(R.id.PaymentAmount);
                String amount = edtEditText.getText().toString();
                if(isNumeric(amount)) {
                    final_amount = Integer.parseInt(amount);
                    if( final_amount !=0){
                        startPayment(final_amount);
                        Intent intent =new Intent(Payments.this,PaymentGateway.class);
                        Payments.this.startActivity(intent);
                    }
                }
                else{
                    Toast.makeText(Payments.this,"Please enter a valid amount.", Toast.LENGTH_LONG).show();
                }
            }
        });
    }

    public static boolean isNumeric(String str) {
        return str.matches("\\d+(\\.\\d+)?");  //match a number with optional '-' and decimal.
    }

    public void startPayment(int amount){
        Checkout checkout = new Checkout();

   /*
   *
   * Set the log
   * checkout.setImage(R.drawable.logo)
   * */

    final Activity activity = this;

    try {
        JSONObject options = new JSONObject();

        options.put("name","Merchant Name");
        options.put("description","Order 1234");
        options.put("currency","INR");
        options.put("amount",amount*100);
        checkout.open(activity,options);
    }catch (Exception e) {
        e.printStackTrace();
        Log.e("Payment",e.toString());
    }
    }

    @Override
    public void onPaymentSuccess(String razorPayPaymentID){
        Toast.makeText(this, "Payment Successful", Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onPaymentError(int code, String response) {
//        Toast.makeText(this, "Payment Error", Toast.LENGTH_SHORT).show();
    }

}
