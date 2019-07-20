package com.example.android.fundraiser;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class Payments extends AppCompatActivity {

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
                Toast.makeText(getApplicationContext(), amount, Toast.LENGTH_LONG).show();
                Intent intent =new Intent(Payments.this,PaymentGateway.class);
                Payments.this.startActivity(intent);
//                OpenGateway(msg);
            }
        });
    }
}
