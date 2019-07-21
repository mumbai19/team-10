package com.example.android.fundraiser;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class LoginActivity extends AppCompatActivity {

    EditText email, password;
    Button btnlogin;
    TextView tvRegister;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

//        Toast.makeText(this,"YO",Toast.LENGTH_LONG).show();
        email = (EditText) findViewById(R.id.et_email);
        password = (EditText) findViewById(R.id.et_password);
        btnlogin = (Button) findViewById(R.id.logsbutton);
        btnlogin.setOnClickListener(new View.OnClickListener(){
            @Override
            public  void onClick(View view) {
//                Toast.makeText(view.getContext(),"YO",Toast.LENGTH_LONG).show();
//                setContentView(R.layout.main);
                Intent chart=new Intent(LoginActivity.this,MainActivity.class);
                LoginActivity.this.startActivity(chart);
            }
        });
    }

}