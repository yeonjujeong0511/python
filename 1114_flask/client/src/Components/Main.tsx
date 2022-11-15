import axios from "axios";
import { useEffect, useState } from "react";

type company = {
  no: number;
  market: string;
  code: string;
  name: string;
  startday: string;
  realSearch: string;
  flotationNY: string;
};

type companyResponse = {
  data: company[];
};

const Main = () => {
  const [companyData, setCompanyData] = useState([]);

  useEffect((): any => {
    try {
      axios
        .get<companyResponse>("/company", {
          headers: {
            Accept: "application/json",
          },
        })
        .then((response: any) => {
          setCompanyData(response.data);
          console.log(response);
        });
    } catch (error) {
      if (axios.isAxiosError(error)) {
        console.log("error message : ", error.message);
        return error.message;
      } else {
        console.log("unexpected error : ", error);
        return "An unexpected error occurred";
      }
    }
  }, []);

  return (
    <>
      <h1>DB연동</h1>
      {companyData.map((element: any) => (
        <div>
          <p>
            {element.no} {element.market} - {element.name} - {element.code} -
            {element.startday}
          </p>
        </div>
      ))}
    </>
  );
};

export default Main;
