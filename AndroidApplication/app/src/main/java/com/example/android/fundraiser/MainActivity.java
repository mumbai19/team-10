package com.example.android.fundraiser;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private final static int REQUEST_CODE_1 = 1;
//    private final static int   = 1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

        ImageButton img = (ImageButton) findViewById(R.id.WomenEmpowermentImage);
        img.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(MainActivity.this, "Click", Toast.LENGTH_LONG).show();
//                String msg = "This message comes from PassingDataSourceActivity's first button";
                Intent intent =new Intent(MainActivity.this,Payments.class);
                MainActivity.this.startActivity(intent);
//                OpenGateway(msg);
            }
        });
    }
//
//    private void OpenGateway(String msg) {
//        Intent intent = new Intent(MainActivity.this, PaymentGateway.class);
//        intent.putExtra("message", msg);
//        startActivityForResult(intent, REQUEST_CODE_1);
//    }
//
//    @Override
//    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
//        super.onActivityResult(requestCode, resultCode, data);
//    }
}
