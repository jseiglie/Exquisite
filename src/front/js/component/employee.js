import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "../../styles/switch.css";
const Employee = () => {
  const [data, setData] = useState([]);
  const navigate = useNavigate();
  useEffect(() => {
    fetch(`${process.env.BACKEND_URL}/api/getEmployee`)
      .then((resp) => resp.json())
      .then((data) => setData(data));
  }, []);

  const handleClick = (e) => {
    console.log(e.target.id);
    navigate(`/employee_details/${e.target.id}`);
  };

  const handleToggle = (e) => {
    console.log(e.target.checked);
  };

  return (
    <>
      <div className="container-fluid d-flex pt-3 bg-white">
        Mostrar solo empleados activos?
        <label className="tog round m-1">
          <input type="checkbox" onChange={(e) => handleToggle(e)} />
          <i></i>
        </label>
      </div>
      <div className="container-fluid bg-white ">
        {data &&
          data.map((el) => (
            <div className="col-sm-6 col-md-4 col-lg-3 col-xl-2 " key={el.id}>
              <div className="card employee-card">
                <div className="card-body employee-card-body">
                  <h5 className="employee-name mb-0">Nombre:</h5>
                  <p className="employee-card-details">{el.fullName}</p>
                  <h5 className="employee-role mb-0">Role:</h5>
                  <p className="employee-card-details">{el.rol}</p>
                </div>
                <div className="card-footer employee-card-footer">
                  <button
                    id={el.id}
                    className="btn btn-secondary employee-card-button"
                    onClick={(e) => handleClick(e)}
                  >
                    Consultar
                  </button>
                </div>
              </div>
            </div>
          ))}
      </div>
    </>
  );
};

export default Employee;
