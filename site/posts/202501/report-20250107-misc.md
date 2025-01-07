---
date: '2025-01-07'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6122406...MicrosoftDocs:7840f69
summary: この文書の更新では、エンティティカテゴリーの名称を「PhoneNumber」から「Phone」に変更しました。また、Visual Studio Codeに関するホスト名とポートに関する情報や、ネットワークの隔離に関する新しい情報が追加されています。新機能としては、Visual
  Studio Codeの利用時に必要なホスト名の具体例や、ネットワーク隔離の設定方法に関する手順が盛り込まれました。破壊的な変更はなく、集合的な更新は、AIサービスや開発環境の設定と管理をより効率的にすることを目的としています。これにより、技術者や管理者は、ネットワークセキュリティを考慮したシステム運用を行えるようになります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:6122406...MicrosoftDocs:7840f69){target="_blank"}

# ハイライト
- "エンティティカテゴリー名称変更"として、「PhoneNumber」から「Phone」に変更。
- Visual Studio Codeのホストとポートに関する追加情報。
- ネットワークの隔離に関する新情報の追加。

## 新機能
- Visual Studio Codeの利用に必要なホスト名とその目的が、具体例と共に追加されました。
- ネットワーク隔離の設定が必要な場合の手順に関する新しいセクションが追加されました。

## 破壊的変更
- 特に破壊的な変更は報告されていません。

## その他の更新
- エンティティ名「PhoneNumber」が「Phone」に変更。
- "ネットワークの隔離"が設定されたプロジェクトの手順についての情報が強化されました。

# インサイト
この一連の文書更新は、利用者がAIサービスや開発環境をより効率的に設定、管理できるようにすることを目的としています。エンティティカテゴリー名称の変更は、APIレスポンスなどでの整合性を確保し、不明確な情報の解消を図っています。Visual Studio Codeに関する追加情報は、リモート開発環境の設定やネットワークの構成手順に対する理解を深めることを狙っており、特にセキュリティや接続性の側面での準備を整えるための助けになります。ネットワークの隔離に関する情報の追加は、ネットワークセキュリティを意識したプロジェクト運営に役立ちます。これらのドキュメントのアップデートにより、技術者や管理者は、より一層正確で詳細な情報を基にして、効果的なシステムの運用が強化されるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [conversations-entity-categories.md](#item-c268ff) | minor update | エンティティカテゴリーの名称変更 | modified | 3 | 3 | 6 | 
| [configure-managed-network.md](#item-dc9c50) | minor update | Visual Studio Codeのホストとポートに関する情報の追加 | modified | 14 | 16 | 30 | 
| [vscode.md](#item-24bd97) | minor update | ネットワークの隔離に関する情報の追加 | modified | 4 | 0 | 4 | 


# Modified Contents
## articles/ai-services/language-service/personally-identifiable-information/concepts/conversations-entity-categories.md{#item-c268ff}

<details>
<summary>Diff</summary>
````diff
@@ -49,23 +49,23 @@ This category contains the following entity:
    :::column-end:::
 :::row-end:::
 
-## Category: PhoneNumber
+## Category: Phone
 
 This category contains the following entity:
 
 :::row:::
     :::column span="":::
         **Entity**
 
-        PhoneNumber
+        Phone
 
     :::column-end:::
     :::column span="2":::
         **Details**
 
         All telephone numbers (including toll-free numbers or numbers that may be easily found or considered public knowledge) are considered PII
 
-        To get this entity category, add `PhoneNumber` to the `pii-categories` parameter. `PhoneNumber` will be returned in the API response if detected.
+        To get this entity category, add `Phone` to the `pii-categories` parameter. `Phone` will be returned in the API response if detected.
       
     :::column-end:::
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "エンティティカテゴリーの名称変更"
}
```

### Explanation
この変更では、文書内の「PhoneNumber」というエンティティカテゴリーの名称が「Phone」に変更されています。具体的には、変更箇所は以下の通りです：

- セクションタイトルの「## Category: PhoneNumber」が「## Category: Phone」に変更されました。
- エンティティ名も同様に、表内の「PhoneNumber」が「Phone」に修正されています。

この変更は、「pii-categories」パラメータに追加する際に、APIレスポンスに返されるという内容にも影響します。このような名称変更は、文書の整合性を保ち、利用者に正確な情報を提供するために重要です。

## articles/ai-studio/how-to/configure-managed-network.md{#item-dc9c50}

<details>
<summary>Diff</summary>
````diff
@@ -774,22 +774,20 @@ To allow installation of __Python packages for training and deployment__, add ou
 Visual Studio Code relies on specific hosts and ports to establish a remote connection.
 
 #### Hosts
-If you plan to use __Visual Studio Code__ with the hub, add outbound _FQDN_ rules to allow traffic to the following hosts:
-
-* `*.vscode.dev`
-* `vscode.blob.core.windows.net`
-* `*.gallerycdn.vsassets.io`
-* `raw.githubusercontent.com`
-* `*.vscode-unpkg.net`
-* `*.vscode-cdn.net`
-* `*.vscodeexperiments.azureedge.net`
-* `default.exp-tas.com`
-* `code.visualstudio.com`
-* `update.code.visualstudio.com`
-* `*.vo.msecnd.net`
-* `marketplace.visualstudio.com`
-* `pkg-containers.githubusercontent.com`
-* `github.com`
+
+The hosts in this section are used to install Visual Studio Code packages to establish a remote connection between Visual Studio Code and the compute instances for your project.
+
+> [!NOTE]
+> This is not a complete list of the hosts required for all Visual Studio Code resources on the internet, only the most commonly used. For example, if you need access to a GitHub repository or other host, you must identify and add the required hosts for that scenario. For a complete list of host names, see [Network Connections in Visual Studio Code](https://code.visualstudio.com/docs/setup/network).
+
+| __Host name__ | __Purpose__ |
+| ---- | ---- |
+| `*.vscode.dev`<br>`*.vscode-unpkg.net`<br>`*.vscode-cdn.net`<br>`*.vscodeexperiments.azureedge.net`<br>`default.exp-tas.com` | Required to access vscode.dev (Visual Studio Code for the Web) |
+| `code.visualstudio.com` | Required to download and install VS Code desktop. This host isn't required for VS Code Web. |
+| `update.code.visualstudio.com`<br>`*.vo.msecnd.net` | Used to retrieve VS Code server bits that are installed on the compute instance through a setup script. |
+| `marketplace.visualstudio.com`<br>`vscode.blob.core.windows.net`<br>`*.gallerycdn.vsassets.io` | Required to download and install VS Code extensions. These hosts enable the remote connection to compute instances. For more information, see [Get started with Azure AI Foundry projects in VS Code](./develop/vscode.md). |
+| `https://github.com/microsoft/vscode-tools-for-ai/tree/master/azureml_remote_websocket_server/*` | Used to retrieve websocket server bits that are installed on the compute instance. The websocket server is used to transmit requests from Visual Studio Code client (desktop application) to Visual Studio Code server running on the compute instance. |
+| `vscode.download.prss.microsoft.com` | Used for Visual Studio Code download CDN |
 
 #### Ports
 You must allow network traffic to ports 8704 to 8710. The VS Code server dynamically selects the first available port within this range.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Visual Studio Codeのホストとポートに関する情報の追加"
}
```

### Explanation
この変更では、Visual Studio Codeを利用するためのホストおよびポートに関する情報が文書に追加されました。変更内容は以下の通りです：

- **ホスト**セクションに、Visual Studio Codeがリモート接続を確立するために必要な特定のホストが挙げられています。このリストは、必須のホスト名とその目的が提示されています。
- 特に、各ホストの使用目的についての詳細が提供されており、例として GitHub リポジトリなどのリソースにアクセスするために必要なホストは個別に特定して追加する必要がある旨も説明されています。
- **注意書き**として、これはインターネット上のすべての Visual Studio Code リソースに必要なホストの完全なリストではないことが記されています。また、ホストの目的についての表が提供されており、各ホストがどのような役割を果たすのかが具体的に説明されています。

これにより、ユーザーは Visual Studio Code を使用する際に必要なネットワーク設定について、より詳細で具体的な情報を得ることができるようになりました。

## articles/ai-studio/how-to/develop/vscode.md{#item-24bd97}

<details>
<summary>Diff</summary>
````diff
@@ -84,6 +84,10 @@ AI app templates are linked from the right side of the **Code** tab of your proj
 
 To provision an entirely new set of resources, including a new hub and project, and deploy these sample applications, you can use the [Azure Developer CLI](/azure/developer/azure-developer-cli/) (AZD) in your local development environment. 
 
+## Use network isolation
+
+If your Azure AI Foundry project is configured for network isolation you may need to open ports to the internet, For more information, visit [How to configure network isolation](../configure-managed-network.md#scenario-use-visual-studio-code).
+
 ## Remarks
 
 If you plan to work across multiple code and data directories, or multiple repositories, you can use the split root file explorer feature in VS Code. To try this feature, follow these steps:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ネットワークの隔離に関する情報の追加"
}
```

### Explanation
この変更では、Azure AI Foundry プロジェクトに関連する「ネットワークの隔離」に関する情報が文書に追加されました。具体的な内容は以下の通りです：

- 新たに「## Use network isolation」というセクションが追加され、ネットワーク隔離が設定されているプロジェクトの場合、外部との接続のためにポートを開く必要があることが説明されています。
- さらに、ネットワーク隔離の設定に関する詳細は、「How to configure network isolation」というリンクを通じて提供されており、ユーザーが必要な手順を確認できるようになっています。

この追加情報により、ユーザーはプロジェクトの設定に応じたネットワーク管理についての理解を深めることができ、適切にリソースを利用するためのサポートが強化されています。


