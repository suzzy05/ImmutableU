import plutusScript from "@/data/plutus.json";
import {
  applyParamsToScript,
  BlockfrostProvider,
  MeshTxBuilder,
  serializePlutusScript,
  UTxO,
} from "@meshsdk/core";

const blockfrostApiKey = import.meta.env.VITE_API_BLOCKFROST_API_KEY;

export function getscript() {
  const scriptCbor = applyParamsToScript(
    plutusScript.validators[0].compiledCode,
    []
  );

  const scriptAddr = serializePlutusScript({
    code: scriptCbor,
    version: "V3",
  }).address;

  return { scriptCbor, scriptAddr };
}

let blockchainProvider: BlockfrostProvider | null = null;

try {
  if (blockfrostApiKey && blockfrostApiKey !== 'previewXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') {
    blockchainProvider = new BlockfrostProvider(blockfrostApiKey);
  }
} catch (error) {
  console.warn('BlockFrost provider initialization failed:', error);
}

export function getTxBuilder() {
  if (!blockchainProvider) {
    throw new Error("BlockFrost provider not initialized. Please configure VITE_API_BLOCKFROST_API_KEY");
  }
  return new MeshTxBuilder({
    fetcher: blockchainProvider,
    submitter: blockchainProvider,
  });
}

// reusable function to get a UTxO by transaction hash
export async function getUtxoByTxHash(txHash: string): Promise<UTxO> {
  if (!blockchainProvider) {
    throw new Error("BlockFrost provider not initialized. Please configure VITE_API_BLOCKFROST_API_KEY");
  }
  const utxos = await blockchainProvider.fetchUTxOs(txHash);
  if (utxos.length === 0) {
    throw new Error("UTxO not found");
  }
  return utxos[0];
}
