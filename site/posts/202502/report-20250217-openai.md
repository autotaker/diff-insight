---
date: '2025-02-17'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1cff62f...MicrosoftDocs:caf7737
summary: この変更は、複数のドキュメントにおいてセキュリティ関連の情報を更新し、Azure Key Vaultの使用を推奨する内容が追加されたものです。プラットフォームごとに、機密情報の安全な保管方法に関する注意事項が改善され、既存の警告文が削除され、説明が統一されています。主に、認証情報の管理に焦点を当て、セキュリティ基準を向上させることを目的としています。これにより、デベロッパやIT管理者がセキュリティポリシーを一貫して管理しやすくなると期待されます。ユーザーはAzure
  Key Vaultを用いた最新のベストプラクティスを容易に導入でき、ドキュメント全体の質も向上します。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1cff62f...MicrosoftDocs:caf7737){target="_blank"}

# ハイライト

この変更は、複数のドキュメントでセキュリティ関連の情報を更新するためのもので、Azure Key Vaultの使用を推奨する情報が追加されています。具体的には、各プラットフォーム（.NET、JavaScript、Python、TypeScript）のドキュメントにおいて、機密情報の安全な保管方法に関する注意事項が改善されました。警告の文章が削除され、Azure Key Vaultに関する説明が統一的に記載されるようになりました。

## 新機能

- Azure Key Vaultの使用を推奨するインクルードが各種ドキュメントに追加。

## 破壊的な変更

- 各ドキュメントから既存の重要警告が削除されているが、セキュリティの観点での重大な欠点を示すものではありません。

## その他の更新

- 不要な空行や冗長な情報を取り除き、ドキュメントが簡潔で明確になるよう改善。

# インサイト

この変更は、主に認証情報の管理に焦点を当てたもので、各ドキュメントにAzure Key Vaultについての情報を追加することにより、セキュリティ基準を向上させています。Azure Key Vaultは、クラウド上での秘密情報の管理を容易にし、より高いセキュリティを提供するサービスとして多くの企業で採用されています。

変更の背景には、APIキーや認証情報の漏えいを防ぐための安全管理が強く求められている現状があると考えられます。ワンクリックでセキュリティを手軽に強化できるAzure Key Vaultを推奨することで、デベロッパやIT管理者はセキュリティポリシーの管理において一貫性を持たせることができます。この一連の更新は、ユーザーがCode Firstの環境でセキュアなプラクティスを容易に取り入れるための支援になります。

各言語のドキュメントで一貫したセキュリティ推奨を提示することで、ドキュメント全体の質も向上し、セキュリティに関する理解が深まるでしょう。この変更により、ユーザーがAzure Key Vaultを使った最新のベストプラクティスを容易に導入できるようになります。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [on-your-data-configuration.md](#item-4875d3) | minor update | データ構成に関するドキュメントの内容更新 | modified | 1 | 2 | 3 | 
| [gpt-v-dotnet.md](#item-120a68) | minor update | gpt-v-dotnet.mdのドキュメント更新 | modified | 1 | 2 | 3 | 
| [gpt-v-javascript.md](#item-a128c9) | minor update | gpt-v-javascript.mdのセキュリティ情報追加 | modified | 1 | 0 | 1 | 
| [gpt-v-python.md](#item-366276) | minor update | gpt-v-python.mdのセキュリティ情報更新 | modified | 1 | 1 | 2 | 
| [gpt-v-typescript.md](#item-03ec34) | minor update | gpt-v-typescript.mdのセキュリティ情報追加 | modified | 1 | 1 | 2 | 
| [text-to-speech-dotnet.md](#item-fea66a) | minor update | text-to-speech-dotnet.mdのセキュリティ情報変更 | modified | 1 | 5 | 6 | 
| [text-to-speech-javascript.md](#item-e9b653) | minor update | text-to-speech-javascript.mdにAzure Key Vaultの情報追加 | modified | 1 | 0 | 1 | 
| [text-to-speech-typescript.md](#item-1335d5) | minor update | text-to-speech-typescript.mdにAzure Key Vaultの情報追加 | modified | 1 | 0 | 1 | 
| [whisper-dotnet.md](#item-562a58) | minor update | whisper-dotnet.mdのセキュリティ勧告の更新 | modified | 1 | 2 | 3 | 
| [whisper-javascript.md](#item-3ee990) | minor update | whisper-javascript.mdの認証情報のセキュリティに関する更新 | modified | 1 | 2 | 3 | 
| [whisper-typescript.md](#item-eafedb) | minor update | whisper-typescript.mdのセキュリティ関連の更新 | modified | 1 | 2 | 3 | 


# Modified Contents
## articles/ai-services/openai/how-to/on-your-data-configuration.md{#item-4875d3}

<details>
<summary>Diff</summary>
````diff
@@ -81,8 +81,7 @@ If you are using a published [web app](./use-web-app.md), you need to redeploy i
 
 When using the API, pass the `filter` parameter in each API request. For example:
 
-> [!IMPORTANT]
-> The following is for example only. If you use an API key, store it securely somewhere else, such as in [Azure Key Vault](/azure/key-vault/general/overview). Don't include the API key directly in your code, and never post it publicly.
+[!INCLUDE [Azure Key Vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
 
 For more information about AI services security, see [Authenticate requests to Azure AI services](/azure/ai-services/authentication).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ構成に関するドキュメントの内容更新"
}
```

### Explanation
この変更は、ドキュメント「on your data configuration.md」の更新です。主に、APIキーの安全な保存方法に関する注意事項が改善されました。具体的には、重要な警告が削除され、新たにAzure Key Vaultに関するインクルードが追加されています。この変更により、ユーザーはAPIキーを安全に管理するための推奨される方法をより明確に理解できるようになります。また、修正により全体の明確さが向上し、関連情報へのリンクも更新されています。変更内容は、全体的に3箇所あり、1行が追加される一方で2行が削除されています。

## articles/ai-services/openai/includes/gpt-v-dotnet.md{#item-120a68}

<details>
<summary>Diff</summary>
````diff
@@ -101,8 +101,7 @@ Passwordless authentication is more secure than key-based alternatives and is th
     Console.WriteLine($"{chatCompletion.Content[0].Text}");
     ```
 
-    > [!IMPORTANT]
-    > For production, store and access your credentials using a secure method, such as [Azure Key Vault](/azure/key-vault/general/overview). For more information about credential security, see [Azure AI services security](../../security-features.md).
+[!INCLUDE [Azure Key Vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/microsoft-entra-id-akv-expanded.md)]
 
 1. Run the application using the `dotnet run` command or the run button at the top of Visual Studio:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "gpt-v-dotnet.mdのドキュメント更新"
}
```

### Explanation
この更新は、ドキュメント「gpt-v-dotnet.md」の内容に関するもので、主に認証情報の管理に関する推奨が改善されました。具体的には、重要な注意事項が削除され、代わりにAzure Key Vaultに関するインクルードが追加されました。この更新により、ユーザーは安全な認証情報の保管方法についてより適切で最新の情報を得られるようになります。全体として、変更箇所は3つあり、1行が追加される一方で2行が削除されています。この改訂は、Azureサービスのセキュリティに関連する内容の明確化を目的としています。

## articles/ai-services/openai/includes/gpt-v-javascript.md{#item-a128c9}

<details>
<summary>Diff</summary>
````diff
@@ -227,6 +227,7 @@ Select an image from the [azure-samples/cognitive-services-sample-data-files](ht
     ```console
     node quickstart.js
     ```
+[!INCLUDE [Azure Key Vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
 
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "gpt-v-javascript.mdのセキュリティ情報追加"
}
```

### Explanation
この変更は、ドキュメント「gpt-v-javascript.md」におけるセキュリティ情報の強化を目的としています。具体的には、Azure Key Vaultに関連するインクルードが1行追加されました。この追加により、ユーザーは認証情報を安全に管理するための推奨される方法をより明確に理解できるようになりました。全体として、変更は1箇所で、コードに関連する実行手順が記載された部分の直後にセキュリティに関する重要な情報が追加されています。これにより、ユーザーはアプリケーションの実行時にセキュリティを意識しやすくなるでしょう。

## articles/ai-services/openai/includes/gpt-v-python.md{#item-366276}

<details>
<summary>Diff</summary>
````diff
@@ -95,7 +95,7 @@ Create a new Python file named _quickstart.py_. Open the new file in your prefer
     ```console
     python quickstart.py
     ```
-
+[!INCLUDE [Azure Key Vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
 
 ## Clean up resources
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "gpt-v-python.mdのセキュリティ情報更新"
}
```

### Explanation
この変更は、「gpt-v-python.md」ドキュメント内におけるセキュリティ情報の更新を目的としています。具体的には、セキュリティに関連する重要な情報としてAzure Key Vaultへのインクルードが追加されました。同時に、不要な空行が削除されています。この更新により、ユーザーはPythonスクリプトの実行時に認証情報を安全に管理するための推奨方法を知ることができ、これによりセキュリティ意識が向上します。全体として、変更は2箇所で、1行が追加され、1行が削除されました。これにより、ドキュメントの可読性も改善されています。

## articles/ai-services/openai/includes/gpt-v-typescript.md{#item-03ec34}

<details>
<summary>Diff</summary>
````diff
@@ -249,7 +249,7 @@ Select an image from the [azure-samples/cognitive-services-sample-data-files](ht
     node quickstart.js
     ```
 
-
+[!INCLUDE [Azure Key Vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
 
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "gpt-v-typescript.mdのセキュリティ情報追加"
}
```

### Explanation
この変更は、「gpt-v-typescript.md」ドキュメントにおけるセキュリティ情報の強化を目的としています。具体的には、Azure Key Vaultに関するインクルードが新たに追加されました。この追加により、ユーザーはアプリケーションのセキュリティを確保するための方法をより明確に理解できるようになります。また、1行が削除されることで、全体のレイアウトが改善されています。この変更によって、ユーザーが安全に認証情報を管理し、コード実行時にセキュリティを意識する助けとなるでしょう。変更は計2箇所で、1行追加され、1行削除されています。

## articles/ai-services/openai/includes/text-to-speech-dotnet.md{#item-fea66a}

<details>
<summary>Diff</summary>
````diff
@@ -43,8 +43,7 @@ To make requests to your Azure OpenAI service, you need the service endpoint as
 - [Microsoft Entra ID](/entra/fundamentals/whatis) is the recommended approach for authenticating to Azure services and is more secure than key-based alternatives. 
 - Access keys allow you to provide a secret key to connect to your resource.
 
-    > [!IMPORTANT]
-    > Access keys should be used with caution. If your service access key is lost or accidentally exposed in an insecure location, your service may become vulnerable. Anyone who has the access key is able to authorize requests against the Azure OpenAI service.
+[!INCLUDE [Azure Key Vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
 
 ### Get the Azure OpenAI endpoint
 
@@ -100,9 +99,6 @@ The access key value can be found in the **Keys & Endpoint** section when examin
     Console.WriteLine("Finished streaming");
     ```
 
-    > [!IMPORTANT]
-    > For production, store and access your credentials using a secure method, such as [Azure Key Vault](/azure/key-vault/general/overview). For more information about credential security, see [Azure AI services security](../../security-features.md).
-
 1. Run the application using the `dotnet run` command or the run button at the top of Visual Studio:
 
     ```dotnetcli
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "text-to-speech-dotnet.mdのセキュリティ情報変更"
}
```

### Explanation
この変更は、「text-to-speech-dotnet.md」ドキュメントのセキュリティ関連情報の見直しを目的としています。主な変更点は、Azure Key Vaultに関する情報が新たに追加され、従来の警告メッセージが削除されたことです。具体的には、アクセスキーに関する重要な注意事項が取り除かれ、代わりにAzure Key Vaultを推奨するインクルードが挿入されました。これにより、ユーザーは秘密情報を安全に管理するための最新の推奨手法を学ぶことができ、セキュリティ意識が高まることが期待されます。全体として、変更は合計で6箇所で行われ、1行が追加され、5行が削除されています。

## articles/ai-services/openai/includes/text-to-speech-javascript.md{#item-e9b653}

<details>
<summary>Diff</summary>
````diff
@@ -176,6 +176,7 @@ Your app's _package.json_ file will be updated with the dependencies.
     });
     
     ```
+[!INCLUDE [Azure Key Vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
 
 1. Run the script with the following command:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "text-to-speech-javascript.mdにAzure Key Vaultの情報追加"
}
```

### Explanation
この変更は、「text-to-speech-javascript.md」ドキュメントにAzure Key Vaultに関する情報を追加することを目的としています。具体的には、セキュリティの観点から、Azure Key Vaultの使用を推奨するインクルードが新たに加えられました。この追加により、ユーザーはアプリケーションの機密情報を安全に管理するための方法をより明確に理解できるようになります。変更は1箇所で、1行の追加が行われています。この小さな更新で、ドキュメントのセキュリティに対する意識向上が期待されます。

## articles/ai-services/openai/includes/text-to-speech-typescript.md{#item-1335d5}

<details>
<summary>Diff</summary>
````diff
@@ -204,4 +204,5 @@ Your app's _package.json_ file will be updated with the dependencies.
     node Text-to-speech.js
     ```
 
+[!INCLUDE [Azure Key Vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
 ---
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "text-to-speech-typescript.mdにAzure Key Vaultの情報追加"
}
```

### Explanation
この変更は、「text-to-speech-typescript.md」ドキュメントにAzure Key Vaultに関する情報を追加することを目的としています。具体的には、機密情報の保護に関する推奨として、Azure Key Vaultの使用を促すインクルードが新たに追加されました。この変更により、ユーザーはアプリケーションの認証情報を安全に管理するための最新のベストプラクティスを理解しやすくなります。変更は1箇所で、1行の追加が行われており、セキュリティ意識の向上が期待されます。

## articles/ai-services/openai/includes/whisper-dotnet.md{#item-562a58}

<details>
<summary>Diff</summary>
````diff
@@ -92,8 +92,7 @@ Passwordless authentication is more secure than key-based alternatives and is th
     }
     ```
 
-    > [!IMPORTANT]
-    > For production, store and access your credentials using a secure method, such as [Azure Key Vault](/azure/key-vault/general/overview). For more information about credential security, see [Azure AI services security](../../security-features.md).
+[!INCLUDE [Azure Key Vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
 
 1. Run the application using the `dotnet run` command or the run button at the top of Visual Studio:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "whisper-dotnet.mdのセキュリティ勧告の更新"
}
```

### Explanation
この変更は、「whisper-dotnet.md」ドキュメントのセキュリティに関する部分を更新することを目的としています。具体的には、認証情報の保存とアクセスに関する重要な警告が削除され、新たにAzure Key Vaultに関連するインクルードが追加されました。この変更により、ユーザーはAzure Key Vaultを通じて認証情報を安全に管理することの重要性をより明確に理解できるようになります。また、不要な情報が削除されたことで、文書がより簡潔になっています。変更の結果、2行が削除され、1行が追加されており、全体のセキュリティガイダンスが強化されています。

## articles/ai-services/openai/includes/whisper-javascript.md{#item-3ee990}

<details>
<summary>Diff</summary>
````diff
@@ -167,8 +167,7 @@ Your app's _package.json_ file will be updated with the dependencies.
 
 You can get sample audio files, such as *wikipediaOcelot.wav*, from the [Azure AI Speech SDK repository at GitHub](https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/master/sampledata/audiofiles).
 
-> [!IMPORTANT]
-> For production, store and access your credentials using a secure method, such as [Azure Key Vault](/azure/key-vault/general/overview). For more information about credential security, see [Azure AI services security](../../security-features.md).
+[!INCLUDE [Azure Key Vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
 
 ## Output
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "whisper-javascript.mdの認証情報のセキュリティに関する更新"
}
```

### Explanation
この変更は、「whisper-javascript.md」ドキュメントの認証情報のセキュリティに関する推奨事項を更新することを目的としています。具体的には、認証情報を安全に保存・アクセスするための重要な警告が削除され、新たにAzure Key Vaultに関連するインクルードが追加されました。これにより、ユーザーは最新のセキュリティプラクティスに基づいて認証情報を管理する方法をより明確に理解できるようになります。また、不要な文言が削除されたことで、ドキュメントが簡潔になり、焦点が絞られています。変更によって計3箇所が修正され、最終的には2行が削除され、1行が追加されています。

## articles/ai-services/openai/includes/whisper-typescript.md{#item-eafedb}

<details>
<summary>Diff</summary>
````diff
@@ -171,8 +171,7 @@ Your app's _package.json_ file will be updated with the dependencies.
 
 You can get sample audio files, such as *wikipediaOcelot.wav*, from the [Azure AI Speech SDK repository at GitHub](https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/master/sampledata/audiofiles).
 
-> [!IMPORTANT]
-> For production, store and access your credentials using a secure method, such as [Azure Key Vault](/azure/key-vault/general/overview). For more information about credential security, see [Azure AI services security](../../security-features.md).
+[!INCLUDE [Azure Key Vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
 
 ## Output
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "whisper-typescript.mdのセキュリティ関連の更新"
}
```

### Explanation
この変更は、「whisper-typescript.md」ドキュメントにおけるセキュリティ関連の情報を更新することを目的としています。具体的には、認証情報を安全に保存およびアクセスするための重要な警告が削除され、Azure Key Vaultに関連するインクルードが追加されています。この更新により、ユーザーはAzure Key Vaultを利用して認証情報を管理する方法について、より明確な指針を得ることができます。また、不要な文言が削除されたことで、ドキュメントがより簡潔で分かりやすくなっています。合計で3箇所が変更され、2行が削除され1行が追加され、全体的な情報の質が向上しています。


