package com.example.demo;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class WebController {

    

    @GetMapping("/")
    public String mostrarInicio(Model model) {
        model.addAttribute("mensaje", "ola ola pasa pasa");
        
        return "inicio"; 
    }

}