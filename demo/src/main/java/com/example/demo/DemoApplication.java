package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.ui.ConcurrentModel;
import org.springframework.ui.Model;

@SpringBootApplication
public class DemoApplication {
    public static void main(String[] args) {
        ConfigurableApplicationContext ctx = SpringApplication.run(DemoApplication.class, args);

        System.out.println("Hola soy Diego este es mi primer proyecto en Spring");

        WebController controlador = ctx.getBean(WebController.class);
        Model model = new ConcurrentModel();
        String vista = controlador.mostrarInicio(model);

        System.out.println("Vista devuelta: " + vista);
        System.out.println("Mensaje: " + model.getAttribute("mensaje"));
        System.out.println("Página disponible en: http://localhost:8080/");
    }
}