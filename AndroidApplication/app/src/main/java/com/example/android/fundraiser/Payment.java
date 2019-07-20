package com.example.android.fundraiser;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

public class Payment extends AppCompatActivity {
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.payment);
        Button pay = (Button)findViewById(R.id.Pay);
        pay.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
//                Toast.makeText(MainActivity.this, "Click", Toast.LENGTH_LONG).show();
//                String msg = "This message comes from PassingDataSourceActivity's first button";
                EditText edtEditText = (EditText)findViewById(R.id.PaymentAmount);
                String amount = edtEditText.getText().toString();
                Intent intent =new Intent(Payment.this,PaymentGateway.class);
                Payment.this.startActivity(intent);
//                OpenGateway(msg);
            }
        });
    }
}
