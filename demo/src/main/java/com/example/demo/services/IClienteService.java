package com.example.demo.services;
import java.util.List;

import com.example.demo.entity.Cliente;

public interface IClienteService {
    public List<Cliente> findAll();
    public Cliente save(Cliente cliente);
    public Cliente findById (Long Id);
    public void delete(Long id);
}