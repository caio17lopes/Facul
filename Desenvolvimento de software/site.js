import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import * as html2pdf from "html2pdf.js";

const salvarContrato = (conteudo) => {
const contratosSalvos = JSON.parse(localStorage.getItem("contratosAmpliar") || "[]");
contratosSalvos.push({ conteudo, data: new Date().toLocaleString() });
localStorage.setItem("contratosAmpliar", JSON.stringify(contratosSalvos));
};

export default function ContractGenerator() {
const [form, setForm] = useState({
    contratante: "",
    cpf: "",
    email: "",
    telefone: "",
    endereco: "",
    data: "",
    materiais: "",
    valorMateriais: "",
    valorMaoDeObra: "",
    dataInstalacao: "",
});
const [contratoGerado, setContratoGerado] = useState("");

const gerarContrato = () => {
    const contrato = `
**CONTRATO DE VENDA E PRESTAÇÃO DE SERVIÇOS**

**Contratada:** Ampliar Pisos Laminado e Vinílicos LTDA, inscrita no CNPJ 24.861.720/0001-00, com sede em [inserir endereço completo].

**Contratante:** ${form.contratante}, CPF: ${form.cpf}, E-mail: ${form.email}, Telefone: ${form.telefone}.

**Objeto do Contrato:**
A contratada se compromete a realizar a entrega e instalação dos seguintes materiais:

${form.materiais}

**Valor e Forma de Pagamento:**
- Materiais: R$ ${form.valorMateriais} (pagos à vista no fechamento do contrato via PIX para a chave 24.861.720/0001-00 – Banco Inter – Razão Social: Caio Vital Lopes).
- Mão de Obra: R$ ${form.valorMaoDeObra} (pagos ao final do serviço, via PIX na mesma chave).

**Local de Entrega e Instalação:**
${form.endereco}

**Data Prevista de Instalação:** ${form.dataInstalacao}

**Cláusula 1 – Escolha do Produto:**
Como os produtos são feitos sob encomenda, o contratante declara estar ciente de que, após o fechamento do contrato, **não será possível alterar ou cancelar o pedido.**

**Cláusula 2 – Prazos de Entrega:**
- Produtos em estoque: entrega conforme combinado para instalação.
- Produtos sob encomenda: 25 dias úteis para piso laminado e 35 dias úteis para piso vinílico.

**Cláusula 3 – Garantia:**
A contratada garante:
- Entrega dos materiais em perfeitas condições.
- Instalação realizada por profissional autorizado da empresa.

**Cláusula 4 – Exclusões de Garantia:**
A garantia não cobre:
- Mau uso (uso de pano molhado, ceras, produtos abrasivos)
- Arranhões, cortes ou impactos
- Calamidades, fenômenos naturais ou infestação de cupins
- Instalações em áreas externas, banheiros ou locais com alta umidade (se o piso não for resistente à água)
- Exposição direta à luz solar
- Aplicação de produtos com cera, silicone ou similares

**Cláusula 5 – Cancelamento:**
Em caso de desistência após o fechamento do contrato, não haverá reembolso dos valores pagos pelos materiais. Caso a desistência ocorra antes da instalação, será cobrada multa de 20% sobre o valor da mão de obra.

*Observação Legal:* Conforme o artigo 49 do Código de Defesa do Consumidor, o direito de arrependimento não se aplica a produtos feitos sob encomenda. A multa estipulada visa cobrir custos administrativos e operacionais e está em conformidade com os princípios da razoabilidade e proporcionalidade previstos na legislação.

**Cláusula 6 – Condições do Local de Instalação:**
O contratante deverá deixar o ambiente de instalação limpo, seco e, preferencialmente, livre de obstáculos ou móveis. Caso não seja possível remover os móveis, a contratada poderá, com bom senso e flexibilidade, realizar o serviço com os móveis no local, desde que não prejudique a qualidade da instalação, ou remarcar o serviço ou cobrar taxa adicional pelo deslocamento dos móveis, conforme avaliação no local.

**Cláusula 7 – Nota Fiscal:**
A contratada se compromete a emitir nota fiscal relativa aos valores pagos por materiais e serviços.

**Cláusula 8 – Foro:**
Fica eleito o foro da Comarca de Conselheiro Lafaiete/MG para dirimir eventuais conflitos, com renúncia de qualquer outro, por mais privilegiado que seja.

---

Declaro estar ciente de todas as cláusulas citadas acima.

**Data:** ${form.data}

**Assinatura do Contratante:** ______________________________________
**Nome:** ${form.contratante}  
**CPF:** ${form.cpf}  
**E-mail:** ${form.email}  
**Telefone:** ${form.telefone}

**Assinatura da Contratada:** ______________________________________
**Caio Vital Lopes – CNPJ: 24.861.720/0001-00 – Tel.: (11) 99526-6655
    `;
    setContratoGerado(contrato);
    salvarContrato(contrato);
};

const baixarPDF = () => {
    const element = document.getElementById("contratoDisplay");
    if (element) {
        html2pdf().set({
        margin: 10,
        filename: "Contrato_Ampliar.pdf",
        html2canvas: { scale: 2 },
        jsPDF: { unit: "mm", format: "a4", orientation: "portrait" },
    }).from(element).save();
    } else {
    console.error("Elemento para gerar PDF não encontrado.");
    }
};

return (
    <div className="p-4 space-y-4 max-w-3xl mx-auto">
    <h1 className="text-2xl font-bold">Gerador de Contratos Ampliar</h1>

    <div className="grid gap-4">
        <div>
            <Label>Nome do Cliente</Label>
            <Input value={form.contratante} onChange={(e) => setForm({ ...form, contratante: e.target.value })} />
        </div>
        <div>
            <Label>CPF</Label>
            <Input value={form.cpf} onChange={(e) => setForm({ ...form, cpf: e.target.value })} />
        </div>
        <div>
            <Label>E-mail</Label>
            <Input value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} />
        </div>
        <div>
            <Label>Telefone</Label>
            <Input value={form.telefone} onChange={(e) => setForm({ ...form, telefone: e.target.value })} />
        </div>
        <div>
            <Label>Endereço da Instalação</Label>
            <Input value={form.endereco} onChange={(e) => setForm({ ...form, endereco: e.target.value })} />
        </div>
        <div>
            <Label>Data do Contrato</Label>
            <Input type="date" value={form.data} onChange={(e) => setForm({ ...form, data: e.target.value })} />
        </div>
        <div>
            <Label>Data da Instalação</Label>
            <Input type="date" value={form.dataInstalacao} onChange={(e) => setForm({ ...form, dataInstalacao: e.target.value })} />
        </div>
        <div>
            <Label>Materiais e Serviços</Label>
            <Textarea value={form.materiais} onChange={(e) => setForm({ ...form, materiais: e.target.value })} />
        </div>
        <div>
            <Label>Valor dos Materiais (R$)</Label>
            <Input value={form.valorMateriais} onChange={(e) => setForm({ ...form, valorMateriais: e.target.value })} />
        </div>
        <div>
            <Label>Valor da Mão de Obra (R$)</Label>
            <Input value={form.valorMaoDeObra} onChange={(e) => setForm({ ...form, valorMaoDeObra: e.target.value })} />
        </div>
    </div>

    <Button className="mt-4" onClick={gerarContrato}>Gerar Contrato</Button>

    {contratoGerado && (
        <div className="mt-6 border rounded p-4 bg-white" id="contratoDisplay">
            <pre className="whitespace-pre-wrap text-sm">{contratoGerado}</pre>
            <Button className="mt-4" onClick={baixarPDF}>Baixar em PDF</Button>
        </div>
        )}
    </div>
    );
}
