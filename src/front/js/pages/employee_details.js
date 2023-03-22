import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
const Employee_details = (props) => {
  const params = useParams();
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch(`${process.env.BACKEND_URL}/api/employee_details/${params.id}`)
      .then((resp) => resp.json())
      .then((data) => {
        console.log(data);
        setData(data);
      });
  }, []);

  return (
    <div className="container-fluid d-flex justify-content-center">
      {data ? (
        <div className="row text-center">
          <h1 className="details-name p-3">{data.fullName}</h1>
          <div className="col-sm-12 col-md-4 col-lg-4 col-xl-4 employee-details_body-left">
            <label htmlFor="fullName">Nombre:</label>
            <input type="text" id="fullName" placeholder={data.fullName} />

            <p>DNI: {data.dni}</p>
            <p>Dirección: {data.address}</p>
            <p>CP: {data.cp}</p>
            <p>Ciudad: {data.city}</p>
            <p>Comunidad: {data.comunity}</p>
            <p>Telefóno: {data.telephone}</p>
            <p>email: {data.email}</p>
            <p>
              Vacaciones: {data.vacations_amount ? data.vacations_amount : 0}
            </p>
          </div>
          <div className="col-sm-12 col-md-4 col-lg-4 col-xl-4 employee-details_body-center">
            <p>rol: {data.rol}</p>
            <p>Horario: {data.schedule}</p>
            <p>Contratado: {data.hired}</p>
            <p>Salario bruto (Anual): {data.brut_salary}</p>
            <p>IRPF: {data.irpf}</p>
            <p>Salario neto (Mensual): {data.net_salary}</p>
            <p>Cantidad de pagos (anual): {data.cuotas}</p>
            <p>{data.fired ? "Despedido: " + data.fired : ""}</p>
          </div>
          <div className="col-sm-12 col-md-4 col-lg-4 col-xl-4 employee-details_body-middle">
            <p>ultimas vacaciones: {data.vacaciones}</p>
            <p>Incidentes: {data.incidents}</p>
            <p>Reportes: {data.reports}</p>
          </div>
        </div>
      ) : (
        ""
      )}
    </div>
  );
};

export default Employee_details;
